def basic_order():
    # TODO: Insert to db retrieve order_id
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
    }


def multiple_products_order():
    # TODO: Insert to db retrieve order_id
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
    }


def high_priority_order():
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
    }


def exceeding_weight_order():
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
    }


def exceeding_volume_order():
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
    }


def multiple_suppliers_order():
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
    }


def invalid_product_order():
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
    }


def invalid_supplier_order():
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
    }


def empty_products_order():
    order = {"order_id": order_id, "warehouse_id": 1, "products": []}
