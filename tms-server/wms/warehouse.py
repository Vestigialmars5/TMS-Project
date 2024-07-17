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
