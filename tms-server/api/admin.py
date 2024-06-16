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
        password = data.get("password")
        role = data.get("role")

        response, status = UserService.create_user(email, password, role)

        return jsonify(response), status


@admin_blueprint.route("/users", methods=("GET",))
def get_users():
    if request.method == "GET":

        search = request.args.get("search", "")
        sort = request.args.get("sort", "asc")
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 25, type=int)

        response, status = UserService.get_users(search, sort, page, limit)

        return jsonify(response), status


@admin_blueprint.route("/users/<int:id>", methods=("DELETE",))
def delete_user(id):
    if request.method == "DELETE":

        response, status = UserService.delete_user(id)

        return jsonify(response), status


@admin_blueprint.route("/users/<int:id>", methods=("PUT",))
def update_user(id):
    if request.method == "PUT":

        data = request.get_json()

        username = data.get("username")
        email = data.get("email")
        role = data.get("role")

        print(username, email, role)

        response, status = UserService.update_user(id, username, email, role)

        return jsonify(response), status
