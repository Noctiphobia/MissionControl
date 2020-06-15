from flask import jsonify, Blueprint, request

from app.api.errors.duplicate_error import DuplicateError
from app.api import repository
from app.components.servers.server_config import ServerConfig

servers_blueprint = Blueprint('api', __name__)


@servers_blueprint.route('/', methods=['GET'])
def list_servers() -> str:
    return jsonify(sorted(list(repository.servers.keys())))


@servers_blueprint.route('/<string:name>', methods=['GET'])
def get_server(name: str) -> str:
    server = repository.servers[name.lower()]
    server.update()
    return jsonify(server.to_dict())


@servers_blueprint.route('/<string:name>', methods=['POST', 'PUT'])
def add_server(name: str) -> str:
    name = name.lower()
    config = ServerConfig(request.json)
    if config.name != name:
        raise AttributeError(f'Name {name} in URL does not match name {config.name} in request body.')
    if request.method == 'POST' and name in repository.servers:
        raise DuplicateError(f'Server {name} already exists.')
    repository.servers[name] = config.get_server()
    return ''

