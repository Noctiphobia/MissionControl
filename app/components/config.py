import json
from typing import Dict, Any, List, Optional

from app.components.servers.game_server import GameServer
from app.components.servers.server_config import ServerConfig


class Config:

    def __init__(self, config_text: Optional[str]) -> None:
        if config_text is None:
            self.servers = []
        else:
            config = json.loads(config_text)
            self.servers = self.load_server_configs(config)

    @staticmethod
    def load_server_configs(config: Dict[str, Any]) -> List[ServerConfig]:
        return [ServerConfig(server_data) for server_data in config['servers']]

    def create_servers(self) -> Dict[str, GameServer]:
        return {server_config.name: server_config.get_server() for server_config in self.servers}
