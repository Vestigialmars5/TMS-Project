from flask import Blueprint, jsonify, render_template, request, url_for
from db import get_db
from werkzeug.security import generate_password_hash

admin_blueprint = Blueprint("admin", __name__, url_prefix="/api/admin")


@admin_blueprint.route("/")
def index():
    return "<p>Hello, World!</p>"


# TODO: Complete this
@admin_blueprint.route("/users", methods=("POST",))
def create_user():
    if request.method == "POST":

        # TODO: Get data from request
        data = request.get_json()

        email = data.get("email")
        username = email.split("@")[0]  # TODO: Make this different for uniqueness
        password = data.get("password")
        role = data.get("role")

        try:
            # TODO: Validations for registering
            if not email or not username or not password or not role:
                raise Exception("something missing")

            db = get_db()
            db.execute(
                "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
                (username, email, generate_password_hash(password), role),
            )
            db.commit()
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    return jsonify({"success": True}), 200


# ADMIN (permision to everything, managing accounts, system config, performance)
# EDIT DATABSE
# ADD USERS
# DELETE ACCOUNTS
# ACCESS TO LOGS
