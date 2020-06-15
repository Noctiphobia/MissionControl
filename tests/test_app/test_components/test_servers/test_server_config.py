from typing import Dict, Type, Callable, Any
from unittest import TestCase

from app.components.servers.game_server import GameServer
from app.components.servers.server_config import ServerConfig


class MockServer(GameServer):

    def __init__(self, mock_param: bool) -> None:
        self.mock_param = mock_param

    def mock_method(self) -> bool:
        return self.mock_param


def with_type_to_class(new_type_to_class: Dict[str, Type]) -> Callable:
    def decorator(function: Callable):
        def wrapper(*args, **kwargs) -> Any:
            old_type_to_class = ServerConfig._type_to_class
            try:
                ServerConfig._type_to_class = new_type_to_class
                return function(*args, **kwargs)
            finally:
                ServerConfig._type_to_class = old_type_to_class
        return wrapper
    return decorator


class TestServerConfig(TestCase):
    @with_type_to_class({'MockServer': MockServer})
    def test_from_dict(self) -> None:
        server_data = {
            'type': 'MockServer',
            'name': 'mock',
            'params': {
                'mock_param': True
            }
        }
        server_config = ServerConfig(server_data)
        instance = server_config.get_server()
        self.assertTrue(hasattr(instance, 'mock_method'))
        self.assertTrue(instance.mock_method())

    @with_type_to_class({'MockServer': MockServer})
    def test_from_dict_fails_for_wrong_data(self) -> None:
        self.assertRaises(AttributeError, lambda: ServerConfig({'type': 'FakeType', 'name': 'fake', 'params': {}}).get_server())
        self.assertRaises(AttributeError, lambda: ServerConfig({'type': 'MockServer'}).get_server())
        self.assertRaises(AttributeError, lambda: ServerConfig({'type': 'MockServer', 'params': {}}).get_server())
