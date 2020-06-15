from typing import Dict, Any, Type

from app.components.servers.game_server import GameServer


class ServerConfig:
    from app.components.servers.minecraft.minecraft_server import MinecraftServer
    _type_to_class = {
        'Minecraft': MinecraftServer
    }

    def __init__(self, server_data: Dict) -> None:
        try:
            self.type: str = server_data['type']
            self.name: str = server_data['name'].lower()
            self.params: Dict[str, Any] = server_data['params']
        except KeyError as e:
            raise AttributeError(f'Could not initialize server config from data: {server_data}', e)

    def get_server(self) -> GameServer:
        try:
            return self._get_server_class(self.type)(**self.params)
        except Exception as e:
            raise AttributeError(f'Could not create server object for: {self}', e)

    def _get_server_class(self, server_type: str) -> Type:
        return self._type_to_class[server_type]

    def __str__(self) -> str:
        return f'type: {self.type}, \nname: {self.name}, \nparams: {self.params}, \nupdate_interval: {self.update_interval}'
