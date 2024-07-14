from flask import Blueprint
from db import get_db
from wms.orders.orders import place_order


wms_blueprint = Blueprint("wms", __name__, url_prefix="/wms")

@wms_blueprint.route("/orders", methods=["GET"])
def testing_orders():
    return place_order("basic")