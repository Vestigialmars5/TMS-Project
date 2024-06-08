from flask import Blueprint, jsonify, render_template, request, url_for
from db import get_db
from werkzeug.security import generate_password_hash

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.route("/")
def index():
    return "<p>Hello, World!</p>"


# TODO: Complete this
@admin_blueprint.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":

        # TODO: Get data from request
        email = "asdf@asdf.com"
        username = email.split("@")[0]
        password = "asdfasdf"
        role = "admin"
        
        # TODO: Validations for registering

        db = get_db()
        try:
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
