from typing import List

from app.components.servers.game_server import GameServer
import mcstatus


class MinecraftServer(GameServer):

    def __init__(self, host: str, port: int = 25565) -> None:
        self.server = mcstatus.MinecraftServer(host, port)
        self.up: bool = False
        self.ping: int = 0
        self.online_players: List[str] = []
        self.max_players: int = 0

    def is_up(self) -> bool:
        return self.up

    def get_ping(self) -> int:
        return self.ping

    def get_online_players(self) -> List[str]:
        return self.online_players

    def get_max_players(self) -> int:
        return self.max_players

    def update(self) -> None:
        try:
            status = self.server.status()
            self.ping = round(status.latency)
            self.max_players = status.players.max
            self.online_players = self.server.query().players.names
            self.up = True
        except Exception:
            self.up = False
            self.ping = 0
            self.online_players = []
