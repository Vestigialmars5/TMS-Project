from ..db import db
from datetime import datetime

class OrdersPlaced(db.Model):
    __tablename__ = "orders_placed"
    __bind_key__ = "wms"

    order_id = db.Column(db.Integer, primary_key=True)
    order_uuid = db.Column(db.String(36), unique=True, nullable=False)
    warehouse_id = db.Column(db.Integer, nullable=False)
    total_weight = db.Column(db.Float, nullable=False)
    total_volume = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f"Order('{self.order_uuid}', '{self.created_at}')"

class OrderProducts(db.Model):
    __tablename__ = "order_products"
    __bind_key__ = "wms"

    order_product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders_placed.order_id"), ondelete="CASCADE")
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    supplier_id = db.Column(db.Integer, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)

    order = db.relationship("OrdersPlaced", backref="order_products")
    product = db.relationship("Products", backref="order_products")

    def __repr__(self):
        return f"OrderDetails('{self.quantity}', '{self.weight}')"
