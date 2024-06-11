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
from flask_jwt_extended import create_access_token, jwt_required, verify_jwt_in_request
from werkzeug.security import check_password_hash
from db import get_db

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# TODO: check auth libraries


# TODO: Complete login
@auth_blueprint.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        print("Headers: ", request.headers)
        print("Payload: ", request.get_json())

        # TODO: Recieve data from request
        db = get_db()
        res = db.execute("SELECT * FROM users WHERE id = ?", (1,))
        row = res.fetchone()

        user_id = row["id"]
        email = row["email"]
        password = row["password"]
        role = row["role"]

        if not validate_login_credentials(email, password):
            return (
                jsonify({"success": False, "error": "Invalid Email Or Password"}),
                401,
            )

        access_token = create_access_token(
            identity=user_id, additional_claims={"email": email, "role": role}
        )

        # Setup session
        perform_login(user_id)

        print("Login successful")
        return jsonify({"success": True, "access_token": access_token}), 200


def perform_login(user_id):
    session.clear()
    session["user_id"] = user_id
    print("User id in session")


# TODO: Complete this
def validate_login_credentials(email, password):
    # TODO: Validations between data being passed and from db
    ############
    return True


# TODO: Check if this function is really needed
# @auth_blueprint.before_app_request
def load_logged_in_user():
    print("Loading in User")
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db()
            .execute("SELECT id, email, role FROM users WHERE id = ?", (user_id,))
            .fetchone()
        )


@auth_blueprint.route("/logout", methods=("GET", "POST"))
def logout():
    if request.method == "POST":
        try:
            verify_jwt_in_request()

            # TODO: Add jti and blacklist for tokens
            session.clear()
            print("Logout successful")
            return jsonify({"success": True}), 200
        except Exception as e:
            print("During logout error:", e)
            return jsonify({"success": False, "error": str(e)}), 400
