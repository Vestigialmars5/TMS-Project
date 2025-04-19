from server.models.tms_models import User, Order, OrderDetails
from tests.utilstest import admin_token, customer_token, token_fixture
from server.extensions import db
import tests.consts as consts
import pytest
import uuid


create_order_test_cases = [
    # Test case 1: Create order with valid inputs
    ("customer_token", "valid", "valid", "Valid Address 123", [{
        "productId": 1,
        "productName": "Carrot",
        "quantity": 1,
        "totalPrice": 10.0,
    }], 201, True),
]


@pytest.mark.parametrize("token_fixture, reference_id, customer_id, delivery_address, order_products, expected_status_code, expected_success", create_order_test_cases, ids=["1"], indirect=["token_fixture"])
def test_create_order(client, token_fixture, reference_id, customer_id, delivery_address, order_products, expected_status_code, expected_success):
    if reference_id == "valid":
        reference_id = str(uuid.uuid4())

    if customer_id == "valid":
        customer_id = db.session.query(User).filter_by(
            email=consts.CUSTOMER_EMAIL).first().user_id

    response = client.post("/api/orders", headers={
        "Authorization": f"Bearer {token_fixture}",
        "Content-Type": "application/json"
    }, json={
        "referenceId": reference_id,
        "customerId": customer_id,
        "deliveryAddress": delivery_address,
        "orderProducts": order_products
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success
