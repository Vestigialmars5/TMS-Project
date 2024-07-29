from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.services.auth_service import AuthService
from ..extensions import db
from ..models.tms_models import User

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

# TODO: check auth libraries
# TODO: Add role based access control


# TODO: Complete login
@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login user
    Expected data: email, password

    @return (dict, int): The response and status code
    """
    if request.method == "POST":
        # Recieve data from request
        data = request.get_json()

        # TODO: Get rid of this, for testing admin
        """res = db.execute("SELECT * FROM users WHERE user_id = ?", (1,))
        row = res.fetchone()
        user_id = row["user_id"]
        email = row["email"]
        password = row["password"]
        role = row["role_id"] """
        try:
            user = db.session.query(User).filter(User.user_id == 1).first()
        except Exception as e:
            return jsonify({"message": str(e)}), 500

        temp_data = {
            "email": user.email,
            "password": user.password,
            "role_id": user.role_id,
            "user_id": user.user_id,
        }

        # TODO: Pass actual data
        response, status = AuthService.login(temp_data)
        return jsonify(response), status


# TODO: Specify what data is, if it is token make it token
@auth_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    Logout user.
    Expected data: token.

    @return (dict, int): The response and status code.
    """
    if request.method == "POST":
        data = request.get_json()
        response, status = AuthService.logout(data)

        return jsonify(response), status


@auth_blueprint.route("/roles", methods=["GET"])
@jwt_required()
def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """
    if request.method == "GET":
        response, status = AuthService.get_roles()

        return jsonify(response), status
