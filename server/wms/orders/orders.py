from server.extensions import db
from server.models.wms_models import OrdersPlaced, OrderProducts
import uuid
import logging
import requests


def place_order(order_type):
    match order_type:
        case "basic":
            order = basic_order()
        case "multiple_products":
            order = multiple_products_order()
        case "high_priority":
            order = high_priority_order()
        case "exceeding_weight":
            order = exceeding_weight_order()
        case "exceeding_volume":
            order = exceeding_volume_order()
        case "multiple_suppliers":
            order = multiple_suppliers_order()
        case "invalid_product":
            order = invalid_product_order()
        case "invalid_supplier":
            order = invalid_supplier_order()
        case "empty_products":
            order = empty_products_order()
        case _:
            return None

    save_order(order["order_id"], order["warehouse_id"], order["products"])

    # Currently both of these functions kinda are redundant
    # But in the future, when the wms isn't part of the same server this will be useful
    send_order(order)  # TODO: Look into a message broker
    return order


def save_order(order_uuid, warehouse_id, products):
    total_weight = 0
    total_volume = 0

    for product in products:
        total_weight += product["weight"]
        total_volume += product["volume"]

    try:
        # Insert order into orders_placed table and get the order_id
        order = OrdersPlaced(order_uuid=order_uuid, warehouse_id=warehouse_id,
                             total_weight=total_weight, total_volume=total_volume)
        db.session.add(order)
        db.session.commit()

        # Create list of all products that will go into the same order and then insert into order_products table
        order_products = []
        for product in products:
            order_products.append(OrderProducts(
                order_id=order.order_id,
                product_id=product["product_id"],
                supplier_id=product["supplier_id"],
                priority=product["priority"],
                quantity=product["quantity"],
                weight=product["weight"],
                volume=product["volume"]
            ))
        db.session.bulk_save_objects(order_products)
        db.session.commit()

    except Exception as e:
        logging.error(e)


def send_order(order):
    print(f"Sending order: {order}")
    try:
        response = requests.post(
            "http://localhost:5000/api/orders", json=order)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def basic_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 1,
        "products": [
            {
                "product_id": 2,
                "product_name": "Steel Beams",
                "supplier_id": 1,
                "priority": 2,
                "quantity": 75,
                "weight": 15,
                "volume": 11.25,
            },
            {
                "product_id": 3,
                "product_name": "Plastic Containers",
                "supplier_id": 1,
                "priority": 3,
                "quantity": 50,
                "weight": 0.5,
                "volume": 1,
            },
        ],
        "total_weight": 15.5,
        "total_volume": 12.25,
    }
    return order


def multiple_products_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 2,
        "products": [
            {
                "product_id": 5,
                "product_name": "Office Supplies",
                "supplier_id": 3,
                "priority": 2,
                "quantity": 20,
                "product_weight": 0.02,
                "product_volume": 0.2,
            },
            {
                "product_id": 6,
                "product_name": "Cleaning Supplies",
                "supplier_id": 3,
                "priority": 3,
                "quantity": 20,
                "product_weight": 0.04,
                "product_volume": 0.4,
            },
            {
                "product_id": 7,
                "product_name": "Cement Bags",
                "supplier_id": 3,
                "priority": 1,
                "quantity": 20,
                "product_weight": 0.66,
                "product_volume": 2,
            },
            {
                "product_id": 8,
                "product_name": "Bricks",
                "supplier_id": 3,
                "priority": 2,
                "quantity": 20,
                "product_weight": 0.036,
                "product_volume": 0.08,
            },
        ],
        "total_weight": 0.756,
        "total_volume": 2.68,
    }
    return order


def high_priority_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 4,
        "products": [
            {
                "product_id": 13,
                "product_name": "Furniture",
                "supplier_id": 6,
                "priority": 1,
                "quantity": 20,
                "weight": 2.4,
                "volume": 12,
            }
        ],
        "total_weight": 2.4,
        "total_volume": 12,
    }
    return order


def exceeding_weight_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 3,
        "products": [
            {
                "product_id": 9,
                "product_name": "Electronics",
                "supplier_id": 4,
                "priority": 3,
                "quantity": 50,
                "weight": 999,
                "volume": 1.5,
            }
        ],
        "total_weight": 999,
        "total_volume": 1.5,
    }
    return order


def exceeding_volume_order():
    order_id = str(uuid.uuid4())
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 1,
        "products": [
            {
                "product_id": 1,
                "product_name": "Heavy Machinery",
                "supplier_id": 1,
                "priority": 1,
                "quantity": 1,
                "weight": 7.5,
                "volume": 999,
            }
        ],
        "total_weight": 7.5,
        "total_volume": 999,
    }
    return order


def multiple_suppliers_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 3,
        "products": [
            {
                "product_id": 7,
                "product_name": "Cement Bags",
                "supplier_id": 3,
                "priority": 1,
                "quantity": 100,
                "weight": 3.3,
                "volume": 10,
            },
            {
                "product_id": 8,
                "product_name": "Bricks",
                "supplier_id": 4,
                "priority": 2,
                "quantity": 1000,
                "weight": 1.8,
                "volume": 4,
            },
        ],
        "total_weight": 5.1,
        "total_volume": 14,
    }
    return order


def invalid_product_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 1,
        "products": [
            {
                "product_id": 99999999,
                "product_name": "Invalid",
                "supplier_id": 1,
                "priority": 1,
                "quantity": 100,
                "weight": 0.3,
                "volume": 4,
            }
        ],
        "total_weight": 0.3,
        "total_volume": 4,
    }
    return order


def invalid_supplier_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 1,
        "products": [
            {
                "product_id": 1,
                "product_name": "Heavy Machinery",
                "supplier_id": 999999,
                "priority": 1,
                "quantity": 1,
                "weight": 7.5,
                "volume": 25,
            }
        ],
        "total_weight": 7.5,
        "total_volume": 25,
    }
    return order


def empty_products_order():
    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "warehouse_id": 1,
        "products": [],
        "total_weight": 0,
        "total_volume": 0,
    }
    return order
