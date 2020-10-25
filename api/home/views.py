from flasgger import swag_from
from flask import Blueprint, g, render_template, current_app as app

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
# @swag_from("/api/docs/home.yml")
def homepage():
    app.logger.info("[HOME] {}: got new request home api".format(g.transaction_id))

    user_name = None

    # Get user from session if it is still logged in

    return render_template("public/index.html", user=user_name), 200


@home.route("/my-profile", methods=["GET"])
# @swag_from("/api/docs/home.yml")
def my_profile():
    app.logger.info("[HOME] {}: got new request home api".format(g.transaction_id))

    user_name = None

    # Get user from session if it is still logged in

    # Get data from user and publish them on the profile page

    return render_template("public/index.html", user=user_name), 200
