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
from flask_jwt_extended import jwt_required, verify_jwt_in_request
from werkzeug.security import check_password_hash
from db import get_db
from services.auth_service import AuthService

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

# TODO: check auth libraries


# TODO: Complete login
@auth_blueprint.route("/login", methods=("POST",))
def login():
    if request.method == "POST":
        print("Headers: ", request.headers)
        print("Payload: ", request.get_json())

        # Recieve data from request
        data = request.get_json()

        # TODO: Get rid of this, for testing admin
        db = get_db()
        res = db.execute("SELECT * FROM users WHERE id = ?", (1,))
        row = res.fetchone()

        user_id = row["id"]
        email = row["email"]
        password = row["password"]
        role = row["role"]

        # TODO: Pass actual data
        response, status = AuthService.login({user_id, email, password, role})

        print("Login successful")
        return jsonify(response), status




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
