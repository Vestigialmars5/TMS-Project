from server.models.tms_models import Role, User, UserDetails
from server.extensions import db
from tests.utilstest import incomplete_user_token
import tests.consts as consts
import pytest
from tests.utilstest import token_fixture


onboard_user_test_cases = [
    # Test case 1: Onboard user with valid inputs
    ("incomplete_user_token", consts.INCOMPLETE_USER_EMAIL, consts.INCOMPLETE_USER_PASSWORD, consts.INCOMPLETE_USER_PASSWORD,
     consts.INCOMPLETE_USER_FIRST_NAME, consts.INCOMPLETE_USER_LAST_NAME,
     consts.INCOMPLETE_USER_PHONE_NUMBER, consts.INCOMPLETE_USER_ADDRESS, consts.INCOMPLETE_USER_ROLE_ID, "valid", 200, True),
]


@pytest.mark.parametrize("token_fixture, email, password, confirmation, first_name, last_name, phone_number, address, role_id, role_name, expected_status_code, expected_success", onboard_user_test_cases, ids=["1"], indirect=["token_fixture"])
def test_onboard_user(client, token_fixture, email, password, confirmation, first_name, last_name, phone_number, address, role_id, role_name, expected_status_code, expected_success):
    if role_name == "valid":
        role_name = db.session.query(Role).filter_by(role_id=role_id).first().role_name
        
    
    response = client.post("/api/onboarding/details", headers={
        "Authorization": f"Bearer {token_fixture}",
        "Content-Type": "application/json"
    }, json={
        "email": email,
        "password": password,
        "confirmation": confirmation,
        "firstName": first_name,
        "lastName": last_name,
        "phoneNumber": phone_number,
        "address": address,
        "role_id": role_id,
        "role_name": role_name
    })

    assert response.status_code == 200
    assert response.json["success"] == expected_success
