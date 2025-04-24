import pytest
import uuid
from server.models.tms_models import User, Order, OrderDetails
from tests.utilstest import token_fixture, TestUtils, customer_token, carrier_token, auth_headers, get_user_id
from server.extensions import db
import tests.consts as consts


class TestOrders:
    """Test cases for order management"""

    @pytest.mark.parametrize(
        "token_fixture, reference_id, customer_id, delivery_address, order_products, expected_status_code, expected_success",
        [
            # Valid order creation
            ("customer_token", "valid", "valid", "Valid Address 123", [{
                "productId": 1,
                "productName": "Carrot",
                "quantity": 1,
                "totalPrice": 10.0,
            }], 201, True),
            # Missing delivery address
            ("customer_token", "valid", "valid", "", [{
                "productId": 1,
                "productName": "Carrot",
                "quantity": 1,
                "totalPrice": 10.0,
            }], 400, False),
            # Empty products array
            ("customer_token", "valid", "valid",
             "Valid Address 123", [], 400, False),
            # No authentication
            ("", "valid", "valid", "Valid Address 123", [{
                "productId": 1,
                "productName": "Carrot",
                "quantity": 1,
                "totalPrice": 10.0,
            }], 401, False),
            # Wrong role (carrier cannot create orders)
            ("carrier_token", "valid", "valid", "Valid Address 123", [{
                "productId": 1,
                "productName": "Carrot",
                "quantity": 1,
                "totalPrice": 10.0,
            }], 401, False),
        ],
        ids=[
            "valid_order_creation",
            "missing_delivery_address",
            "empty_products_array",
            "no_authentication",
            "unauthorized_role"
        ],
        indirect=["token_fixture"]
    )
    def test_create_order(self, client, token_fixture, reference_id, customer_id,
                          delivery_address, order_products, expected_status_code,
                          expected_success, get_user_id, auth_headers):
        """Test creating orders with various inputs"""

        if reference_id == "valid":
            reference_id = str(uuid.uuid4())

        if customer_id == "valid":
            customer_id = get_user_id(consts.CUSTOMER_EMAIL)

        headers = auth_headers(token_fixture)

        response = client.post("/api/orders", headers=headers, json={
            "referenceId": reference_id,
            "customerId": customer_id,
            "deliveryAddress": delivery_address,
            "orderProducts": order_products
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success
        )

    @pytest.mark.parametrize(
        "token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success",
        [
            # Valid request
            ("customer_token", "", "", "asc", 1, 2, 200, True),
            # No authorization
            # Unauthorized role
            # Non-string search (should still work)
            # Invalid sort_by field
            # Invalid sort_order
            # Invalid page number
            # Invalid limit
            # Empty parameters
            # Non-matching search
        ],
        ids=[
            "valid_request",
        ],
        indirect=["token_fixture"]
    )
    def test_get_orders(self, client, token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success, auth_headers):
        """Test retrieving orders with various filtering and sorting options"""

        headers = auth_headers(token_fixture)

        response = client.get(
            f"/api/orders?search={search_field}&sortBy={sort_by}&sortOrder={sort_order}&page={page}&limit={limit}", headers=headers, json={})

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
            expected_fields=["orders"] if expected_success else None
        )
