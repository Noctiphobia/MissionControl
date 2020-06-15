from app.components.config import Config


class ComponentRepository:

    def __init__(self, config: Config) -> None:
        self.servers = config.create_servers()
