from app.components.component_repository import ComponentRepository
from app.components.config import Config

try:
    with open('config.json', 'r') as config_file:
        config = Config(config_file.read())
except IOError:
    config = Config(None)
repository = ComponentRepository(config)
