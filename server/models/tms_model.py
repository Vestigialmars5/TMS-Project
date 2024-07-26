from ..db import db
from datetime import datetime


class Role(db.Model):
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Role('{self.role_name}' id: {self.role_id})"


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(
        "roles.role_id"), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))

    role = db.relationship("Role", backref="users")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class UserDetails(db.Model):
    __tablename__ = "user_details"

    user_detail_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), ondelete="CASCADE")
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(255))

    user = db.relationship("User", backref="user_details")

    def __repr__(self):
        return f"UserDetails('{self.first_name}', '{self.last_name}')"


class DriverDetails:
    __tablename__ = "driver_details"

    driver_detail_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), ondelete="CASCADE")
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    license_expiry = db.Column(db.DateTime, nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeginKey(
        "vehicles.vehicle_id"), nullable=False)
    driver_status = db.Column(db.String(50), nullable=False)

    user = db.relationship("User", backref="driver_details")
    vehicle = db.relationship("Vehicle", backref="driver_details")

    def __repr__(self):
        return f"DriverDetails('{self.license_number}', '{self.driver_status}')"


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_plate = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    fuel_capacity = db.Column(db.Float, nullable=False)
    litres_per_100jkm = db.Column(db.Float, nullable=False)
    tonnage = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Vehicle('{self.vehicle_plate}', '{self.vehicle_type}')"


class Warehouse(db.Model):
    __tablename__ = "warehouses"

    warehouse_id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    docks = db.Column(db.Integer, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    manager = db.relationship("User", backref="warehouses")

    def __repr__(self):
        return f"Warehouse('{self.warehouse_name}', '{self.location}')"


class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    order_uuid = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    order_status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))

    customer = db.relationship("User", backref="orders")

    def __repr__(self):
        return f"Order('{self.order_uuid}', '{self.order_status}')"


class OrderDetails(db.Model):
    __tablename__ = "order_details"

    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "orders.order_id"), ondelete="CASCADE")
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    product_name = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", backref="order_details")
    product = db.relationship("Product", backref="order_details")

    def __repr__(self):
        return f"OrderDetails('{self.quantity}', '{self.price}')"


class Shipment(db.Model):
    __tablename__ = "shipments"

    shipment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "orders.order_id"), ondelete="CASCADE")
    customer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"))
    warehouse_id = db.Column(
        db.Integer, db.ForeignKey("warehouses.warehouse_id"))
    status = db.Column(db.String(50), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    created_at = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))

    order = db.relationship("Order", backref="shipments")
    customer = db.relationship("User", backref="shipments")
    driver = db.relationship("User", backref="shipments")
    vehicle = db.relationship("Vehicle", backref="shipments")
    warehouse = db.relationship("Warehouse", backref="shipments")

    def __repr__(self):
        return f"Shipment('{self.status}', '{self.origin}', '{self.destination}')"


class Invoice(db.Model):
    __tablename__ = "invoices"

    invoice_id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey(
        "shipments.shipment_id"), ondelete="CASCADE")
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))

    shipment = db.relationship("Shipment", backref="invoices")

    def __repr__(self):
        return f"Invoice('{self.amount}', '{self.status}', '{self.due_date}')"


class Payment(db.Model):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey(
        "invoices.invoice_id"), ondelete="CASCADE")
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    status = db.Column(db.String(50), nullable=False)

    invoice = db.relationship("Invoice", backref="payments")

    def __repr__(self):
        return f"Payment('{self.amount}', '{self.status}', '{self.payment_date}')"


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    action = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    details = db.Column(db.String(255))

    user = db.relationship("User", backref="audit_logs")

    def __repr__(self):
        return f"AuditLog('{self.action}', '{self.timestamp}')"


class Report(db.Model):
    __tablename__ = "reports"

    report_id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    generated_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    created_at = db.Column(
        db.DateTime, default=datetime.now(datetime.timezone.utc))
    data = db.Column(db.String(255))

    user = db.relationship("User", backref="reports")

    def __repr__(self):
        return f"Report('{self.report_type}', '{self.created_at}')"
