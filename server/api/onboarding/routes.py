from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from server.api.onboarding import services
from server.utils.data_cleanup import data_cleanup_onboarding

onboarding_blueprint = Blueprint(
    "onboarding", __name__, url_prefix="/api/onboarding")


@onboarding_blueprint.route("/details", methods=["POST"])
@jwt_required()
def onboard_user():
    try:
        data = request.get_json()
    except Exception as e:
        abort(400, description="Invalid JSON")

    user_id = get_jwt_identity()

    email, password, confirmation, first_name, last_name, phone_number, address = data_cleanup_onboarding(data)

    response = services.onboard_user(
        user_id,
        email,
        password,
        confirmation,
        first_name,
        last_name,
        phone_number,
        address
    )

    if response["success"]:
        return jsonify(response), 200
    elif response["error"] == "User Already Onboarded":
        return jsonify(response), 409
    elif response["error"] == "Passwords Do Not Match":
        return jsonify(response), 400
    else:
        return jsonify(response), 500
