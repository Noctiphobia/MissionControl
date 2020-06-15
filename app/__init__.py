from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    from app.api.servers import servers_blueprint
    app.register_blueprint(servers_blueprint, url_prefix='/api/servers')
    return app


app = create_app()
from app.api.errors.error_handlers import *
