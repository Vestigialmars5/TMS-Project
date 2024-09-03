import tests.consts as consts
from utilstest import admin_token
import pytest


# Test Cases
test_cases = [
    # Test case 1: Login with valid inputs
    (consts.ADMIN_EMAIL, consts.ADMIN_PASSWORD, 200, True),
    # Test case 2: Login with invalid email
    (consts.INVALID_EMAIL, consts.ADMIN_PASSWORD, 400, False),
    # Test case 3: Login with invalid password
    (consts.ADMIN_EMAIL, consts.INVALID_PASSWORD, 400, False),
    # Test case 4: Login with no inputs
    ("", "", 400, False),
    # Test case 5: Login with incorrect password
    (consts.ADMIN_EMAIL, consts.CARRIER_PASSWORD, 401, False),
    # Test case 6: Login with incorrect email
    ("i_dont_exist@gmail.com", consts.ADMIN_PASSWORD, 401, False)
]


@pytest.mark.parametrize("email, password, expected_status_code, expected_success", test_cases, ids=["1", "2", "3", "4", "5", "6"])
def test_login(client, admin_token, email, password, expected_status_code, expected_success):
    response = client.post("/api/auth/login", json={
        "email": email,
        "password": password
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success


def logout(client, token):
    response = client.post("/api/auth/logout", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={})

    return response


def test_logout(client, admin_token):
    # Test case 1: Logout with valid token
    response = logout(client, admin_token)

    assert response.status_code == 200
    assert response.json["success"] == True
