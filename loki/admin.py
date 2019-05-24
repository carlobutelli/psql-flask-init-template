from flask import Blueprint, jsonify, g

from flask import current_app as app

from loki import get_db

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/ping")
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
    return jsonify("pong"), 200


@admin.route("/healthcheck")
def health_check_db():
    """
    Healthcheck endpoint checking if db service is available
    Main purpose is to respond to k8s liveness/readyness probes
    ---
    tags:
        - healthcheck
    responses:
        200:
            description: Everything is working well
        500:
            description: At least one of the dependencies is not available. Check logs
    """
    transaction_id = g.transaction_id
    app.logger.info("{}: got new request for DB healthcheck".format(transaction_id))
    db = get_db()
    try:
        # Dummy request to check if database is available
        db.session.execute('SELECT 1')
        app.logger.info("{}: Database is healthy".format(transaction_id))
        return jsonify(status="healthy"), 200
    except Exception as e:
        app.logger.error("{}: unhealthy healthcheck: {}".format(transaction_id, e))
        return jsonify(status="unhealthy", message="Error connecting to database: {}".format(e)), 500
