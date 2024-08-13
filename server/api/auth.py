from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required
from server.services import auth_service
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
        # Receive data from request
        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            abort(400, description="Missing Data")

        # TODO: Pass actual data
        response = auth_service.login(email, password)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Invalid Credentials":
            return jsonify(response), 401
        else:
            return jsonify(response), 500


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
        # Validations -> abort(400, description="Missing Data")

        response = auth_service.logout(data)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500


@auth_blueprint.route("/roles", methods=["GET"])
@jwt_required()
def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """
    if request.method == "GET":

        # Validations -> abort(400, description="Missing Data")        

        response = auth_service.get_roles()

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500

