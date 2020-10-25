from flasgger import swag_from
from flask import Blueprint, g, redirect, render_template, request, current_app as app

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
# @swag_from("/api/docs/login.yml")
def login():
    app.logger.info("[SIGNUP] {}: got new request to login user".format(g.transaction_id))

    if request.method == "POST":

        missing = list()

        for k, v in request.form.items():
            if v == "":
                missing.append(k)

        if missing:
            message = f"Please fill in: {', '.join(missing)}"
            return render_template("login.html", message=message), 400

        email = request.form.get("email")
        password = request.form.get("password")

        print(f'email -----> {email})')
        print(f'password --> {password}')

        return redirect(request.url)

    return render_template("login.html"), 200


@auth.route("/logout", methods=["POST"])
# @swag_from("/api/docs/logout.yml")
def logout():
    app.logger.info("[SIGNUP] {}: got new request to logout user".format(g.transaction_id))

    # destroy the session and redirect to login

    return render_template("login.html"), 200


@auth.route("/sign-up", methods=["GET", "POST"])
# @swag_from("/api/docs/sign-up.yml")
def signup():
    app.logger.info("[SIGNUP] {}: got new request to sign up new user".format(g.transaction_id))

    if request.method == "POST":

        missing = list()

        for k, v in request.form.items():
            if v == "":
                missing.append(k)

        if missing:
            message = f"Please fill in: {', '.join(missing)}"
            return render_template("signup.html", message=message), 400

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        print(f'username --> {username}')
        print(f'email -----> {email})')
        print(f'password --> {password}')

        # save user to the database
        return render_template("login.html"), 200

    # if GET render template to allow user to sign up
    return render_template("signup.html"), 200
