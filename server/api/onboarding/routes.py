from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from server.api.onboarding import services
from server.utils.data_cleanup import data_cleanup_onboarding_user_details, data_cleanup_customer
from server.utils.helpers import get_user_role_id
from server.utils.consts import RoleType

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

    operations = services.BaseOperations()
    response = operations.onboard_user_details(
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


@onboarding_blueprint.route("/step", methods=["GET"])
@jwt_required()
def get_current_step():
    user_id = get_jwt_identity()

    step = services.get_onboarding_step(user_id)

    return jsonify({
        "step": step,
        "success": step != -1
    }), 200 if step != -1 else 400


@onboarding_blueprint.route("/role", methods=["POST"])
@jwt_required()
def onboard_role_details():
    try:
        data = request.get_json()
    except Exception as e:
        abort(400, description="Invalid JSON")

    user_id = get_jwt_identity()

    try:
        role_id = get_user_role_id(user_id)
    except Exception as e:
        abort(400, description="Error Retrieving User Role")

    operations = services.get_order_operations(role_id)

    # Admin
    if role_id == RoleType.ADMIN.id:
        response = operations.onboard_details(user_id, role_id)

    # Transportation Manager
    elif role_id == RoleType.TRANSPORTATION_MANAGER.id:
        response = operations.onboard_details(user_id, role_id)

    # Carrier
    elif role_id == RoleType.CARRIER.id:
        response = operations.onboard_details(user_id, role_id)

    # Customer
    elif role_id == RoleType.CUSTOMER.id:
        company_name, company_address = data_cleanup_customer(
            data)

        response = operations.onboard_details(
            user_id, role_id, company_name, company_address)

    # Driver
    elif role_id == RoleType.DRIVER.id:
        response = operations.onboard_details(user_id, role_id)

    # Accounting
    elif role_id == RoleType.ACCOUNTING.id:
        response = operations.onboard_details(user_id, role_id)

    # Warehouse Manager
    elif role_id == RoleType.WAREHOUSE_MANAGER.id:
        response = operations.onboard_details(user_id, role_id)

    # Dispatcher
    elif role_id == RoleType.DISPATCHER.id:
        response = operations.onboard_details(user_id, role_id)

    # Customer Service Representative
    elif role_id == RoleType.CSR.id:
        response = operations.onboard_details(user_id, role_id)
    else:
        abort(400, description="Invalid Role Name")

    if response["success"]:
        return jsonify(response), 200
    elif response["error"] == "User Already Onboarded" or response["error"] == "Wrong Step":
        return jsonify(response), 409
    else:
        return jsonify(response), 500
