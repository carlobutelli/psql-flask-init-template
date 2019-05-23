import os
import sys
import logging
import uuid

from flask import Flask, request, g
from flask_cors import CORS

from loki.config import DevelopmentConfig, LocalConfig, TestingConfig, ProductionConfig
from loki.exceptions import WrongConfiguration
from loki.core.db_manager import get_db

AVAILABLE_ENVS = {
    "Local": LocalConfig,
    "Testing": TestingConfig,
    "Development": DevelopmentConfig,
    "Production": ProductionConfig
}


def create_app():
    def _get_environment(var_name):
        """Get the environment variable or return exception."""
        try:
            return os.environ[var_name]
        except KeyError:
            error_message = f"Environment {var_name} does not exist, going with development"
            raise WrongConfiguration(error_message)

    def _set_env(var_name):
        if var_name in AVAILABLE_ENVS:
            env = f"loki.config.{var_name}Config"
            return env
        else:
            return "loki.config.DevelopmentConfig"

    try:
        env_aux = _get_environment("ENV")
        ENV = _set_env(env_aux)
    except WrongConfiguration:
        ENV = 'loki.config.DevelopmentConfig'

    # instantiate the app
    app = Flask(__name__)
    cors = CORS()

    # set config
    app.config.from_object(ENV)

    # db = get_db()

    with app.app_context():
        if app.config["ENV"] == "Development":
            cors.init_app(app)

    # register app blueprints
    app.logger.info("[WARMUP]: Registering Blueprints")
    from .views import loki as loki_bp
    app.register_blueprint(loki_bp)
    app.logger.info("[WARMUP]: successfully registered Blueprints")

    # shell context for flask cli
    app.shell_context_processor({'app': app})

    # log handler
    log_level = logging.INFO if not app.config.get('DEBUG') else logging.DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))

    logging.getLogger('flask_cors').level = logging.DEBUG

    for h in app.logger.handlers:
        app.logger.removeHandler(h)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.logger.info("[WARMUP]: Loki app successfully instantiated")

    @app.before_request
    def set_transaction_id():
        transaction_id = request.headers.get("x-request-id")
        g.transaction_id = transaction_id if transaction_id else str(uuid.uuid4().hex)

    return app
