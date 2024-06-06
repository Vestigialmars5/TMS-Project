import functools

from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# TODO: check auth libraries
# TODO: Implement jwt


@auth_blueprint.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not validate_login_credentials(email, password):
            return (
                jsonify({"success": False, "error": "Invalid Email Or Password"}),
                401,
            )

        perform_login(email)

        return jsonify({"success": True}), 200


def perform_login(email):
    session.clear()

    # TODO: Get user id
    session["user_id"] = 1


def validate_login_credentials(email, password):
    # TODO: Validations between data being passed and from db
    ############
    return True


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@auth_blueprint.route("/logout", methods=("GET", "POST"))
def logout():
    session.clear()
    return redirect(url_for("index"))
