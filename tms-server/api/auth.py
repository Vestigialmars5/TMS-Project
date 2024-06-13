from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import get_db
from services.auth_service import AuthService

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

# TODO: check auth libraries


# TODO: Complete login
@auth_blueprint.route("/login", methods=("POST",))
def login():
    if request.method == "POST":
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
        temp_data = {
            "user_id": user_id,
            "email": email,
            "password": password,
            "role": role,
        }

        # TODO: Pass actual data
        response, status = AuthService.login(temp_data)
        print(response, status)

        print("Login successful")
        return jsonify(response), status


@auth_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    if request.method == "POST":
        data = request.get_json()
        response, status = AuthService.logout(data)

        return jsonify(response), status
