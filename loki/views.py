from flask import Blueprint, jsonify, g

from flask import current_app as app

loki = Blueprint("loki", __name__,)


@loki.route("/ping")
def ping_route():
    """
    Example endpoint for testing readiness from the application. Returns a simple pong
    ---
    responses:
      200:
        description: A static >>pong<<
    """
    transaction_id = g.transaction_id
    app.logger.info("[PING] {}: got new request for ping".format(transaction_id))
    return jsonify("pong")
