from server.models.tms_models import *
from server.models.wms_models import *
from server.extensions import db
import pytest


class TestModels:
    """Test cases for database models to verify structure and relationships."""

    def test_tms_models_tables(self, client):
        """Verify TMS model table names match expected database structure."""
        model_tables = {
            Role: "roles",
            User: "users",
            UserDetails: "user_details",
            DriverDetails: "driver_details",
            Vehicle: "vehicles",
            Warehouse: "warehouses",
            Order: "orders",
            OrderDetails: "order_details",
            Product: "products",
            Shipment: "shipments",
            Invoice: "invoices",
            Payment: "payments",
            AuditLog: "audit_logs",
            Report: "reports"
        }

        for model, expected_table in model_tables.items():
            assert model.__tablename__ == expected_table, f"Wrong table name for {model.__name__}"

    def test_tms_database_state(self, client):
        """Verify initial database state for TMS models after setup."""
        assert db.session.query(Role).count() == 7, "Expected 7 roles"
        assert db.session.query(User).count() == 6, "Expected 6 users"

    def test_wms_models_tables(self, client):
        """Verify WMS model table names match expected database structure."""
        model_tables = {
            OrdersPlaced: "orders_placed",
            OrderProducts: "order_products"
        }

        for model, expected_table in model_tables.items():
            assert model.__tablename__ == expected_table, f"Wrong table name for {model.__name__}"
