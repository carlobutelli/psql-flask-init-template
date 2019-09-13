import os
import sys
import logging
import uuid

from flasgger import Swagger
from flask import Flask, request, g
from flask_cors import CORS

from mars.config import DevelopmentConfig, LocalConfig, TestingConfig, ProductionConfig
from mars.exceptions import WrongConfiguration


def create_app():
    app = Flask(__name__)

    cors = CORS(app)

    app_settings = f"mars.config.{os.getenv('FLASK_ENV').capitalize()}Config"
    app.config.from_object(app_settings)

    with app.app_context():
        if app.config["ENV"] == "Development":
            cors.init_app(app)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    # log handler
    log_level = logging.INFO if not app.config.get("DEBUG") else logging.DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s "
        "[in %(pathname)s:%(lineno)d]"
    ))

    logging.getLogger("flask_cors").level = logging.DEBUG

    for h in app.logger.handlers:
        app.logger.removeHandler(h)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.logger.info("[WARMUP]: Registering Blueprints")
    from .admin import admin as admin_bp
    app.register_blueprint(admin_bp)

    app.logger.info("[WARMUP]: successfully registered Blueprints")

    Swagger(app,
            template={
                "swagger": "2.0",
                "info": {
                    "title": "Contract Signing",
                    "version": "1.0.0",
                    "contact": {
                        "email": "c.butelli@nxchange.com"
                    },
                    "description": "API to digitally sign a pdf file"
                },
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "definitions": {
                    "BaseResponse": {
                        "properties": {
                            "status": {
                                "type": "string",
                            },
                            "status_code": {
                                "type": "number",
                            },
                            "message": {
                                "type": "string"
                            },
                            "transaction_id": {
                                "type": "string"
                            }
                        },
                        "type": "object"
                    }
                }
            },
            config={
                "headers": [
                ],
                "specs": [
                    {
                        "endpoint": 'apispec_1',
                        "route": '/apispec_1.json',
                        "rule_filter": lambda rule: True,  # all in
                        "model_filter": lambda tag: True,  # all in
                    }
                ],
                "static_url_path": "/flasgger_static",
                "swagger_ui": True,
                "specs_route": "/swagger/"
            }
            )

    app.logger.info("[WARMUP]: Mars app successfully instantiated")

    @app.before_request
    def set_transaction_id():
        transaction_id = request.headers.get("x-request-id")
        g.transaction_id = transaction_id if transaction_id else str(uuid.uuid4().hex)

    @app.after_request
    def allow_origin(response):
        response.headers["Access-Control-Allow-Origin"] = '*'
        response.headers["Access-Control-Allow-Credentials"] = "true"

        return response

    return app
