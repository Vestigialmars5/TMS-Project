# Receive and process orders from the WMS 

from flask import request, Blueprint
from db import get_db

orders_blueprint = Blueprint("orders", __name__, url_prefix="/orders")


# Listens for orders sent by the WMS
@orders_blueprint.route("/", methods=["POST"])
def receive_order():
    if request.method == "POST":
        data = request.get_json()

        order_uuid = data.get("order_id") # When communicating with the wms, refer to the uuid
        warehouse_id = data.get("warehouse_id")
        products = data.get("products")
        total_weight = data.get("total_weight")
        total_volume = data.get("total_volume")

        # Save the order to the database
        save_order(order_uuid, warehouse_id, products, total_weight, total_volume)


# Save the order to the database


# Function to decide what vehicle type best suits the order (knapsack problem variant)
def decide_vehicle_type(total_weight, total_volume):
