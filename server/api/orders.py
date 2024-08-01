# Receive and process orders from the WMS

from flask import request, Blueprint
from server.extensions import db
from server.models.tms_models import Order, OrderDetails

orders_blueprint = Blueprint("orders", __name__, url_prefix="/orders")


# Listens for orders sent by the WMS
@orders_blueprint.route("/", methods=["POST"])
def receive_order():
    if request.method == "POST":
        data = request.get_json()

        # When communicating with the wms, refer to the uuid
        order_uuid = data.get("order_id")
        warehouse_id = data.get("warehouse_id")
        products = data.get("products")
        total_weight = data.get("total_weight")
        total_volume = data.get("total_volume")

        # Save the order to the database
        save_order(order_uuid, warehouse_id, products,
                   total_weight, total_volume)


# Save the order to the database
def save_order(order_uuid, warehouse_id, products, total_weight, total_volume):
    order = Order(order_uuid=order_uuid, customer_id=)