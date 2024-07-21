from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.jwt_config import jwt
from server.services.profile_service import ProfileService

profile_blueprint = Blueprint("profile", __name__, url_prefix="/api/profile")


@profile_blueprint.route("/user", methods=["GET"])
def get_user():
    """
    Get the user profile.

    @return (dict, int): The response and status code.
    """


    response, status = {"hi": "hi"}, 200

    return jsonify(response), status


@profile_blueprint.route("/user", methods=["PUT"])
@jwt_required()
def update_user():
    """
    Update the user profile.

    @return (dict, int): The response and status code.
    """

    user_id = get_jwt_identity()
    data = request.get_json()
    print(data)

    email = data.get("email")
    password = data.get("password")
    confirmation = data.get("confirmation")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    phone_number = data.get("phoneNumber")
    address = data.get("address")

    print(user_id, email, password, confirmation, first_name, last_name, phone_number, address)

    response, status = ProfileService.update_profile(
        user_id,
        email,
        password,
        confirmation,
        first_name,
        last_name,
        phone_number,
        address,
    )

    return jsonify(response), status
