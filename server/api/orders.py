# Receive and process orders from the WMS 

from flask import request, Blueprint
from server.db import get_db

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
def save_order(order_uuid, warehouse_id, products, total_weight, total_volume):
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(
            """INSERT INTO orders (order_uuid, warehouse_id, total_weight, total_volume) VALUES (?, ?, ?, ?)""", (order_uuid, warehouse_id, total_weight, total_volume)
        )

        order_id = cursor.lastrowid

        for product in products:
            cursor.execute(
                """INSERT INTO order_products (order_id, product_id, product_name, supplier_id, priority, quantity, weight, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (order_id, product["product_id"], product["product_name"], product["supplier_id"], product["priority"], product["quantity"], product["weight"], product["volume"])
            )
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    
    finally:
        cursor.close()
    


