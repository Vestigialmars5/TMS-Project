from server.models.tms_models import *
from server.models.wms_models import *
from server.extensions import db


def test_tms_models(client):
    assert Role.__tablename__ == "roles"
    assert User.__tablename__ == "users"
    assert UserDetails.__tablename__ == "user_details"
    assert DriverDetails.__tablename__ == "driver_details"
    assert Vehicle.__tablename__ == "vehicles"
    assert Warehouse.__tablename__ == "warehouses"
    assert Order.__tablename__ == "orders"
    assert OrderDetails.__tablename__ == "order_details"
    assert Shipment.__tablename__ == "shipments"
    assert Invoice.__tablename__ == "invoices"
    assert Payment.__tablename__ == "payments"
    assert AuditLog.__tablename__ == "audit_logs"
    assert Report.__tablename__ == "reports"
    assert db.session.query(Role).count() == 7
    assert db.session.query(User).count() == 1


def test_wms_models(client):
    assert OrdersPlaced.__tablename__ == "orders_placed"
    assert OrderProducts.__tablename__ == "order_products"