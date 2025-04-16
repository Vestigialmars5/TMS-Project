from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.utils.authorization_decorators import roles_required
from server.utils.data_cleanup import data_cleanup_create_order
from server.api.orders import services

orders_blueprint = Blueprint(
    "orders_blueprint", __name__, url_prefix="/api/orders")


@orders_blueprint.route("/orders", methods=["POST"])
@jwt_required()
@roles_required("Customer")
def create_order():
    if request.method == "POST":
        initiator_id = get_jwt_identity()
        # Get data from request
        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        reference_id, customer_id, delivery_address, order_products = data_cleanup_create_order(
            data)

        response = services.create_order(
            reference_id, customer_id, delivery_address, order_products, initiator_id)

        if response["success"]:
            return jsonify(response), 201
        elif response["error"] == "Unique Constraint Violation":
            return jsonify(response), 409
        else:
            return jsonify(response), 500
