from abc import abstractmethod
from typing import List, Dict, Any
from app.components.component import Component


class GameServer(Component):

    @abstractmethod
    def is_up(self) -> bool:
        pass

    @abstractmethod
    def get_ping(self) -> int:
        pass

    @abstractmethod
    def get_online_players(self) -> List[str]:
        pass

    @abstractmethod
    def get_max_players(self) -> int:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    def to_dict(self) -> Dict[str, Any]:
        return {
            'up': self.is_up(),
            'ping': self.get_ping(),
            'online_players': self.get_online_players(),
            'max_players': self.get_max_players()
        }
