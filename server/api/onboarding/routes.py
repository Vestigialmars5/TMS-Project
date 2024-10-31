from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from server.api.onboarding import services
from server.utils.data_cleanup import data_cleanup_onboarding_user_details, data_cleanup_customer

onboarding_blueprint = Blueprint(
    "onboarding", __name__, url_prefix="/api/onboarding")


@onboarding_blueprint.route("/details", methods=["POST"])
@jwt_required()
def onboard_user_details():
    try:
        data = request.get_json()
    except Exception as e:
        abort(400, description="Invalid JSON")

    user_id = get_jwt_identity()

    email, password, confirmation, first_name, last_name, phone_number, address = data_cleanup_onboarding_user_details(
        data)

    response = services.onboard_user_details(
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
    elif response["error"] == "User Already Onboarded" or response["error"] == "Wrong Step":
        return jsonify(response), 409
    elif response["error"] == "Passwords Do Not Match":
        return jsonify(response), 400
    else:
        return jsonify(response), 500


@onboarding_blueprint.route("/<int:role_id>", methods=["POST"])
@jwt_required()
def onboard_role_details(role_id):
    try:
        data = request.get_json()
    except Exception as e:
        abort(400, description="Invalid JSON")

    user_id = get_jwt_identity()

    # Admin
    if role_id == 1:
        pass

    # Transportation Manager
    elif role_id == 2:
        pass

    # Carrier
    elif role_id == 3:
        pass

    # Customer
    elif role_id == 4:
        company_name, company_address = data_cleanup_customer(
            data)

        response = services.onboard_customer_details(
            user_id, role_id, company_name, company_address)

    # Driver
    elif role_id == 5:
        pass

    # Finance/Accounting
    elif role_id == 6:
        pass

    # Warehouse Manager
    elif role_id == 7:
        pass
    else:
        abort(400, description="Invalid Role Name")

    if response["success"]:
        return jsonify(response), 200
    elif response["error"] == "User Already Onboarded" or response["error"] == "Wrong Step":
        return jsonify(response), 409
    else:
        return jsonify(response), 500
