from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from server.services import onboarding_service
from server.utils.data_cleanup import data_cleanup_onboarding

onboarding_blueprint = Blueprint(
    "onboarding", __name__, url_prefix="/api/onboarding")


@onboarding_blueprint.route("/onboard", methods=["POST"])
@jwt_required()
def onboard_user():
    user_id = get_jwt_identity()
    data = request.get_json()
    claims = get_jwt()

    email = data.get("email")
    password = data.get("password")
    confirmation = data.get("confirmation")
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    phone_number = data.get("phoneNumber")
    address = data.get("address")
    role_id = claims["roleId"]
    role_name = claims["roleName"]

    # Validations -> abort(400, description="Missing Data")

    response = onboarding_service.onboard_user(
        user_id,
        email,
        password,
        confirmation,
        first_name,
        last_name,
        phone_number,
        address,
        role_id,
        role_name,
    )

    if response["success"]:
        return jsonify(response), 200
    elif response["error"] == "User Already Onboarded":
        return jsonify(response), 409
    else:
        return jsonify(response), 500
