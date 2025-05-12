from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.utils.authorization_decorators import roles_required
from server.utils.data_cleanup import data_cleanup_customer_create_order, data_cleanup_search, data_cleanup_customer_sort_orders, data_cleanup_customer_get_order_details
from server.api.orders import services

orders_blueprint = Blueprint("orders_blueprint", __name__, url_prefix="/api")


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

        reference_id, customer_id, delivery_address, order_products = data_cleanup_customer_create_order(
            data)

        response = services.customer_create_order(
            reference_id, customer_id, delivery_address, order_products, initiator_id)

        if response["success"]:
            return jsonify(response), 201
        elif response["error"] == "Invalid Data":
            return jsonify(response), 400
        elif response["error"] == "Not Found":
            return jsonify(response), 404
        elif response["error"] == "Unique Constraint Violation":
            return jsonify(response), 409
        else:
            return jsonify(response), 500


@orders_blueprint.route("/orders", methods=["GET"])
@jwt_required()
@roles_required("Customer")
def get_orders():
    if request.method == "GET":

        search, page, limit = data_cleanup_search(
            request.args)

        sort_by, sort_order = data_cleanup_customer_sort_orders(request.args)

        initiator_id = get_jwt_identity()

        response = services.customer_get_orders(
            search, sort_by, sort_order, page, limit, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500


@orders_blueprint.route("/orders/details", methods=["GET"])
@jwt_required()
@roles_required("Customer")
def get_order_details():
    if request.method == "GET":

        order_id = data_cleanup_customer_get_order_details(request.args)

        initiator_id = get_jwt_identity()

        response = services.get_order_details(
            order_id, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Not Found":
            return jsonify(response), 404
        else:
            return jsonify(response), 500


@orders_blueprint.route("/orders/<int:order_id>", methods=["PUT"])
@jwt_required()
@roles_required("Customer")
def update_order(order_id):
    if request.method == "PUT":
        initiator_id = get_jwt_identity()

        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        reference_id, customer_id, delivery_address, order_products = data_cleanup_customer_update_order(data)

        response = services.customer_update_order()

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Invalid Data":
            return jsonify(response), 400
        elif response["error"] == "Not Found":
            return jsonify(response), 404
        elif response["error"] == "Unique Constraint Violation":
            return jsonify(response), 409
        else:
            return jsonify(response), 500


@orders_blueprint.route("/orders/<int:order_id>", methods=["DELETE"])
@jwt_required()
@roles_required("Customer")
def delete_order(order_id):
    if request.method == "DELETE":
        initiator_id = get_jwt_identity()

        response = services.customer_delete_order(order_id, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Not Found":
            return jsonify(response), 404
        else:
            return jsonify(response), 500
