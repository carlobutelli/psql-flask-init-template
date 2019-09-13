from flask import Blueprint, jsonify, g

from flask import current_app as app

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/ping")
def ping():
    """
    Ping
    Example endpoint for testing readiness from the application. Returns a simple pong
    ---
    responses:
      200:
        description: A static >>pong<<
    """
    transaction_id = g.transaction_id
    app.logger.info("[PING] {}: got new request for ping".format(transaction_id))
    return jsonify("pong"), 200
