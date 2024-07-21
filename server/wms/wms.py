from flask import jsonify, render_template, request, Blueprint
from server.db import get_db
from server.wms.orders.orders import place_order


wms_blueprint = Blueprint("wms", __name__, url_prefix="/wms")

# Renders wms control
@wms_blueprint.route("/")
def wms_controller():
    return render_template("wms.html")


@wms_blueprint.route("/orders", methods=["POST"])
def create_order():
    order_type = request.form.get("order_type")
    print(order_type)
    order = place_order(order_type)
    if order:
        return jsonify({"success": True})
    return jsonify({"success": False})
