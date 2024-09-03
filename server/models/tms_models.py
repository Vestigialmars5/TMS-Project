from ..extensions import db
from datetime import datetime, timezone
from .base import Base1
from sqlalchemy import Index


class Role(Base1):
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)

    __table_args__ = (
        Index('ix_role_name', 'role_name'),
    )

    def __repr__(self):
        return f"Role('{self.role_name}' id: {self.role_id})"


class User(Base1):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(
        "roles.role_id"), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc))

    role = db.relationship("Role", backref="users")
    user_details = db.relationship("UserDetails", backref="UserDetails", uselist=False)

    __table_args__ = (
        Index('ix_email', 'email'),
        Index('ix_role_id', 'role_id'),
        Index('ix_user_status', 'status')
    )

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "role_id": self.role_id,
            "role_name": self.role.role_name,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def to_dict_js(self):
        return {
            "userId": self.user_id,
            "email": self.email,
            "roleId": self.role_id,
            "roleName": self.role.role_name,
            "status": self.status,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }

    def __repr__(self):
        return f"User(''{self.email}', '{self.status}')"


class UserDetails(Base1):
    __tablename__ = "user_details"

    user_detail_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id", ondelete="CASCADE"))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(255))

    __table_args__ = (
        Index('ix_user_details_user_id', 'user_id'),
    )

    def __repr__(self):
        return f"UserDetails('{self.first_name}', '{self.last_name}')"


class DriverDetails(Base1):
    __tablename__ = "driver_details"

    driver_detail_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id", ondelete="CASCADE"))
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    license_expiry = db.Column(db.DateTime, nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey(
        "vehicles.vehicle_id"), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    user = db.relationship("User", backref="driver_details")
    vehicle = db.relationship("Vehicle", backref="driver_details")

    __table_args__ = (
        Index('ix_driver_details_user_id', 'user_id'),
        Index('ix_license_number', 'license_number'),
        Index('ix_vehicle_id', 'vehicle_id')
    )

    def __repr__(self):
        return f"DriverDetails('{self.license_number}', '{self.status}')"


class Vehicle(Base1):
    __tablename__ = "vehicles"

    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_plate = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    fuel_capacity = db.Column(db.Float, nullable=False)
    litres_per_100km = db.Column(db.Float, nullable=False)
    tonnage = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    __table_args__ = (
        Index('ix_vehicle_plate', 'vehicle_plate'),
        Index('ix_vehicle_type', 'vehicle_type'),
        Index('ix_vehicle_status', 'status')
    )

    def __repr__(self):
        return f"Vehicle('{self.vehicle_plate}', '{self.vehicle_type}')"


class Warehouse(Base1):
    __tablename__ = "warehouses"

    warehouse_id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    docks = db.Column(db.Integer, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    manager = db.relationship("User", backref="warehouses")

    __table_args__ = (
        Index('ix_warehouse_name', 'warehouse_name'),
        Index('ix_warehouse_location', 'location')
    )

    def __repr__(self):
        return f"Warehouse('{self.warehouse_name}', '{self.location}')"


class Order(Base1):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    order_uuid = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc))

    customer = db.relationship("User", backref="orders")

    __table_args__ = (
        Index('ix_order_uuid', 'order_uuid'),
        Index('ix_order_customer_id', 'customer_id'),
        Index('ix_order_status', 'status')
    )

    def __repr__(self):
        return f"Order('{self.order_uuid}', '{self.status}')"


class OrderDetails(Base1):
    __tablename__ = "order_details"

    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "orders.order_id", ondelete="CASCADE"))
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", backref="order_details")

    __table_args__ = (
        Index('ix_order_id', 'order_id'),
        Index('ix_product_id', 'product_id'),
        Index('ix_priority', 'priority')
    )

    def __repr__(self):
        return f"OrderDetails('{self.quantity}', '{self.price}')"


class Shipment(Base1):
    __tablename__ = "shipments"

    shipment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "orders.order_id", ondelete="CASCADE"))
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
        db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc))

    order = db.relationship("Order", backref="shipments")
    customer = db.relationship("User", foreign_keys=[
                               customer_id], backref="customer_shipments")
    driver = db.relationship("User", foreign_keys=[
                             driver_id], backref="driver_shipments")
    vehicle = db.relationship("Vehicle", backref="shipments")
    warehouse = db.relationship("Warehouse", backref="shipments")

    __table_args__ = (
        Index('ix_shipment_order_id', 'order_id'),
        Index('ix_shipment_customer_id', 'customer_id'),
        Index('ix_driver_id', 'driver_id'),
        Index('ix_shipment_vehicle_id', 'vehicle_id'),
        Index('ix_warehouse_id', 'warehouse_id'),
        Index('ix_shipment_status', 'status')
    )

    def __repr__(self):
        return f"Shipment('{self.status}', '{self.origin}', '{self.destination}')"


class Invoice(Base1):
    __tablename__ = "invoices"

    invoice_id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey(
        "shipments.shipment_id", ondelete="CASCADE"))
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc))

    shipment = db.relationship("Shipment", backref="invoices")

    __table_args__ = (
        Index('ix_shipment_id', 'shipment_id'),
        Index('ix_invoice_status', 'status')
    )

    def __repr__(self):
        return f"Invoice('{self.amount}', '{self.status}', '{self.due_date}')"


class Payment(Base1):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey(
        "invoices.invoice_id", ondelete="CASCADE"))
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    status = db.Column(db.String(50), nullable=False)

    invoice = db.relationship("Invoice", backref="payments")

    __table_args__ = (
        Index('ix_invoice_id', 'invoice_id'),
        Index('ix_payment_status', 'status')
    )

    def __repr__(self):
        return f"Payment('{self.amount}', '{self.status}', '{self.payment_date}')"


class AuditLog(Base1):
    __tablename__ = "audit_logs"

    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    action = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    details = db.Column(db.String(255))
    email = db.Column(db.String(100), nullable=True)

    user = db.relationship("User", backref="audit_logs")

    def __init__(self, action, user_id=None, email=None, details=""):
        self.user_id = user_id
        self.email = email
        self.action = action
        self.details = details

    def __repr__(self):
        return f"AuditLog('{self.action}', '{self.timestamp}, '{self.details}', user_id: {self.user_id}', email: {self.email}')"


class Report(Base1):
    __tablename__ = "reports"

    report_id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    generated_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc))
    data = db.Column(db.String(255))

    user = db.relationship("User", backref="reports")

    def __repr__(self):
        return f"Report('{self.report_type}', '{self.created_at}')"
