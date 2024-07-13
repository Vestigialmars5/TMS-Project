LOCATIONS = [
    "84 Services Rd, Selkirk, NY 12158",
    "64 Van Patten Dr, Clifton Park, NY 12065",
    "2236 Liberty Dr, Niagara Falls, NY 14304",
    "120 Benson Pl, Frankfort, NY 13340",
    "6823 Industrial Park Rd, Bath, NY 14810",
    "10212 Church Rd N, Utica, NY 13502",
    "4645 Crossroads Park Dr, Liverpool, NY 13088",
    "93 Broadway, Menands, NY 12204" "1650 Niagara Falls Blvd, Tonawanda, NY 14150",
    "11 Rotterdam Industrial Park, Rotterdam, NY 12306"
    "276 McGuinness Blvd, Brooklyn, NY 11222",
]

WAREHOUSES = [
    ("warehouse_0", "64 Van Patten Dr, Clifton Park, NY 12065", 4754), 
    ("warehouse_1", "11 Rotterdam Industrial Park, Rotterdam, NY 12306276 McGuinness Blvd, Brooklyn, NY 11222", 1748), 
    ("warehouse_2", "120 Benson Pl, Frankfort, NY 13340", 3620), 
    ("warehouse_3", "1650 Niagara Falls Blvd, Tonawanda, NY 14150", 2833)]

SUPPLIERS = [
    ("supplier_0", "93 Broadway, Menands, NY 12204"),
    ("supplier_1", "84 Services Rd, Selkirk, NY 12158"),
    ("supplier_2", "4645 Crossroads Park Dr, Liverpool, NY 13088"),
    ("supplier_3", "6823 Industrial Park Rd, Bath, NY 14810"),
    ("supplier_4", "10212 Church Rd N, Utica, NY 13502"),
    ("supplier_5", "4645 Crossroads Park Dr, Liverpool, NY 13088"),
    ("supplier_6", "2236 Liberty Dr, Niagara Falls, NY 14304"),
]


warehouse1 = {
    "warehouse_id": 1,
    "name": "Warehouse A",
    "location": "64 Van Patten Dr, Clifton Park, NY 12065",
    "docks": 5,
    "inventory": [
        {"product_id": 1, "product_name": "Heavy Machinery", "quantity": 10, "reorder_level": 5, "product_weight": 7.5, "product_volume": 25},
        {"product_id": 2, "product_name": "Steel Beams", "quantity": 200, "reorder_level": 50, "product_weight": 0.2, "product_volume": 0.15},
        {"product_id": 3, "product_name": "Plastic Containers", "quantity": 500, "reorder_level": 100, "product_weight": 0.01, "product_volume": 0.02},
        {"product_id": 4, "product_name": "Wooden Pallets", "quantity": 300, "reorder_level": 80, "product_weight": 0.02, "product_volume": 0.1}
    ]
}

warehouse2 = {
    "warehouse_id": 2,
    "name": "Warehouse B",
    "location": "11 Rotterdam Industrial Park, Rotterdam, NY 12306",
    "docks": 3,
    "inventory": [
        {"product_id": 5, "product_name": "Office Supplies", "quantity": 1000, "reorder_level": 200, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 6, "product_name": "Cleaning Supplies", "quantity": 800, "reorder_level": 200, "product_weight": 0.002, "product_volume": 0.02},
        {"product_id": 7, "product_name": "Cement Bags", "quantity": 300, "reorder_level": 100, "product_weight": 0.033, "product_volume": 0.1},
        {"product_id": 8, "product_name": "Bricks", "quantity": 5000, "reorder_level": 1000, "product_weight": 0.0018, "product_volume": 0.004}
    ]
}

warehouse3 = {
    "warehouse_id": 3,
    "name": "Warehouse C",
    "location": "120 Benson Pl, Frankfort, NY 13340",
    "docks": 4,
    "inventory": [
        {"product_id": 9, "product_name": "Electronics", "quantity": 500, "reorder_level": 100, "product_weight": 0.006, "product_volume": 0.03},
        {"product_id": 10, "product_name": "Batteries", "quantity": 2000, "reorder_level": 500, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 11, "product_name": "Books", "quantity": 3000, "reorder_level": 1000, "product_weight": 0.001, "product_volume": 0.004},
        {"product_id": 12, "product_name": "Stationery", "quantity": 4000, "reorder_level": 1500, "product_weight": 0.0005, "product_volume": 0.002}
    ]
}

warehouse4 = {
    "warehouse_id": 4,
    "name": "Warehouse D",
    "location": "1650 Niagara Falls Blvd, Tonawanda, NY 14150",
    "docks": 6,
    "inventory": [
        {"product_id": 13, "product_name": "Furniture", "quantity": 100, "reorder_level": 20, "product_weight": 0.12, "product_volume": 0.6},
        {"product_id": 14, "product_name": "Large Appliances", "quantity": 50, "reorder_level": 10, "product_weight": 0.16, "product_volume": 0.5},
        {"product_id": 15, "product_name": "Medical Supplies", "quantity": 1000, "reorder_level": 300, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 16, "product_name": "Pharmaceuticals", "quantity": 1500, "reorder_level": 500, "product_weight": 0.0008, "product_volume": 0.008}
    ]
}

supplier1 = {
    "supplier_id": 1,
    "name": "Supplier X",
    "location": "93 Broadway, Menands, NY 12204",
    "products": [
        {"product_id": 1, "product_name": "Heavy Machinery", "available_quantity": 50, "product_weight": 7.5, "product_volume": 25},
        {"product_id": 2, "product_name": "Steel Beams", "available_quantity": 1000, "product_weight": 0.2, "product_volume": 0.15},
        {"product_id": 3, "product_name": "Plastic Containers", "available_quantity": 2000, "product_weight": 0.01, "product_volume": 0.02},
        {"product_id": 4, "product_name": "Wooden Pallets", "available_quantity": 1500, "product_weight": 0.02, "product_volume": 0.1}
    ]
}

supplier2 = {
    "supplier_id": 2,
    "name": "Supplier Y",
    "location": "84 Services Rd, Selkirk, NY 12158",
    "products": [
        {"product_id": 3, "product_name": "Plastic Containers", "available_quantity": 2000, "product_weight": 0.01, "product_volume": 0.02},
        {"product_id": 4, "product_name": "Wooden Pallets", "available_quantity": 1500, "product_weight": 0.02, "product_volume": 0.1},
        {"product_id": 5, "product_name": "Office Supplies", "available_quantity": 5000, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 6, "product_name": "Cleaning Supplies", "available_quantity": 3000, "product_weight": 0.002, "product_volume": 0.02}
    ]
}

supplier3 = {
    "supplier_id": 3,
    "name": "Supplier Z",
    "location": "4645 Crossroads Park Dr, Liverpool, NY 13088",
    "products": [
        {"product_id": 5, "product_name": "Office Supplies", "available_quantity": 5000, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 6, "product_name": "Cleaning Supplies", "available_quantity": 3000, "product_weight": 0.002, "product_volume": 0.02},
        {"product_id": 7, "product_name": "Cement Bags", "available_quantity": 1000, "product_weight": 0.033, "product_volume": 0.1},
        {"product_id": 8, "product_name": "Bricks", "available_quantity": 10000, "product_weight": 0.0018, "product_volume": 0.004}
    ]
}

supplier4 = {
    "supplier_id": 4,
    "name": "Supplier W",
    "location": "6823 Industrial Park Rd, Bath, NY 14810",
    "products": [
        {"product_id": 7, "product_name": "Cement Bags", "available_quantity": 1000, "product_weight": 0.033, "product_volume": 0.1},
        {"product_id": 8, "product_name": "Bricks", "available_quantity": 10000, "product_weight": 0.0018, "product_volume": 0.004},
        {"product_id": 9, "product_name": "Electronics", "available_quantity": 500, "product_weight": 0.006, "product_volume": 0.03},
        {"product_id": 10, "product_name": "Batteries", "available_quantity": 2000, "product_weight": 0.001, "product_volume": 0.01}
    ]
}

supplier5 = {
    "supplier_id": 5,
    "name": "Supplier V",
    "location": "10212 Church Rd N, Utica, NY 13502",
    "products": [
        {"product_id": 9, "product_name": "Electronics", "available_quantity": 500, "product_weight": 0.006, "product_volume": 0.03},
        {"product_id": 10, "product_name": "Batteries", "available_quantity": 2000, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 11, "product_name": "Books", "available_quantity": 3000, "product_weight": 0.001, "product_volume": 0.004},
        {"product_id": 12, "product_name": "Stationery", "available_quantity": 4000, "product_weight": 0.0005, "product_volume": 0.002}
    ]
}

supplier6 = {
    "supplier_id": 6,
    "name": "Supplier U",
    "location": "4645 Crossroads Park Dr, Liverpool, NY 13088",
    "products": [
        {"product_id": 11, "product_name": "Books", "available_quantity": 3000, "product_weight": 0.001, "product_volume": 0.004},
        {"product_id": 12, "product_name": "Stationery", "available_quantity": 4000, "product_weight": 0.0005, "product_volume": 0.002},
        {"product_id": 13, "product_name": "Furniture", "available_quantity": 100, "product_weight": 0.12, "product_volume": 0.6},
        {"product_id": 14, "product_name": "Large Appliances", "available_quantity": 50, "product_weight": 0.16, "product_volume": 0.5}
    ]
}

supplier7 = {
    "supplier_id": 7,
    "name": "Supplier T",
    "location": "2236 Liberty Dr, Niagara Falls, NY 14304",
    "products": [
        {"product_id": 13, "product_name": "Furniture", "available_quantity": 100, "product_weight": 0.12, "product_volume": 0.6},
        {"product_id": 14, "product_name": "Large Appliances", "available_quantity": 50, "product_weight": 0.16, "product_volume": 0.5},
        {"product_id": 15, "product_name": "Medical Supplies", "available_quantity": 1000, "product_weight": 0.001, "product_volume": 0.01},
        {"product_id": 16, "product_name": "Pharmaceuticals", "available_quantity": 1500, "product_weight": 0.0008, "product_volume": 0.008}
    ]
}


def heavy_order_high_priority():
    # TODO: Insert to db retrieve order_id
    order = {
        "order_id": order_id,
        "warehouse_id": 2,
        "supplier_id": 5,
        "products": [
            {
                "product_id": 1,
                "product_name": "Heavy Machinery",
                "quantity": 2,
                "priority": 1,
                "weight": 15,
                "volume": 50,
            },
            {
                "product_id": 2,
                "product_name": "Steel Beams",
                "quantity": 50,
                "priority": 1,
                "weight": 4,
                "volume": 30,
            },
        ],
    }


def heavy_order_medium_priority():
    pass

def heavy_order_low_priority():
    pass
