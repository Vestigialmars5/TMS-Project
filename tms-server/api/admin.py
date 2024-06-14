from flask import Blueprint, jsonify, render_template, request, url_for
from db import get_db
from werkzeug.security import generate_password_hash
from services.user_service import UserService

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


@admin_blueprint.route("/users", methods=("GET",))
def get_users():
    if request.method == "GET":
        try:
            search = request.args.get("search", "")
            sort = request.args.get("sort", "asc")
            page = request.args.get("page", 1, type=int)
            limit = request.args.get("limit", 25, type=int)

        except:
            print("Error handlining request parameters")
            return jsonify({"success": False, "error": "error setting variables"}), 200

        response, status = UserService.get_users(search, sort, page, limit)

        return jsonify(response), status
        