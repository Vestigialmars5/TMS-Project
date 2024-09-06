from server.models.tms_models import User
from tests.utilstest import admin_token, carrier_token, token_fixture
from server.extensions import db
import tests.consts as consts
import pytest

create_user_test_cases = [
    # Test case 1: Create user with valid inputs
    ("admin_token", "new@gmail.com", "newnewnew", 1, 201, True),
    # Test case 2: Create user with existing email
    ("admin_token", consts.ADMIN_EMAIL, consts.ADMIN_PASSWORD,
     consts.ADMIN_ROLE_ID, 409, False),
    # Test case 3: Create user with invalid email
    ("admin_token",
     consts.INVALID_EMAIL, "password", 1, 400, False),
    # Test case 4: Create user with invalid password
    ("admin_token", "new@gmail.com", "short", 1, 400, False),
    # Test case 5: Create user with invalid role_id
    ("admin_token", "new@gmail.com",
     "newnewnew", 100, 400, False),
    # Test case 6: Create user with no inputs
    ("admin_token", "", "", 0, 400, False),
    # Test case 7: Create user with no email
    ("admin_token", "", "password", 1, 400, False),
    # Test case 8: Create user with no password
    ("admin_token", "new@gmail.com", "", 1, 400, False),
    # Test case 9: Create user with no role_id
    ("admin_token", "new@gmail.com", "newnewnew", 0, 400, False),
    # Test case 10: Create user with no token
    ("", "new@gmail.com", "newnewnew", 1, 401, False),
    # Test case 11: Create user with invalid token
    ("carrier_token", "new@gmail.com", "newnewnew", 1, 401, False)
]


@pytest.mark.parametrize("token_fixture, email, password, role_id, expected_status_code, expected_success", create_user_test_cases, ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"], indirect=["token_fixture"])
def test_create_user(client, token_fixture, email, password, role_id, expected_status_code, expected_success):
    response = client.post("/api/admin/users", headers={
        "Authorization": f"Bearer {token_fixture}",
        "Content-Type": "application/json"
    }, json={
        "email": email,
        "password": password,
        "roleId": role_id
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success


get_users_test_cases = [
    # Test case 1: Get users with valid inputs
    ("admin_token", "admin", "email", "asc", 1, 2, 200, True),
    # Test case 2: Get users with no token
    ("", "admin", "email", "asc", 1, 2, 401, False),
    # Test case 3: Get users with invalid token
    ("carrier_token", "admin", "email", "asc", 1, 2, 401, False),
    # Test case 4: Get users with invalid search
    ("admin_token", 1, "email", "asc", 1, 2, 200, True),
    # Test case 5: Get users with invalid sort_by
    ("admin_token", "admin", "invalid_sort_by", "asc", 1, 2, 200, True),
    # Test case 6: Get users with invalid sort_order
    ("admin_token", "admin", "email", "invalid_sort_order", 1, 2, 200, True),
    # Test case 7: Get users with invalid page
    ("admin_token", "admin", "email", "asc", 0, 2, 200, True),
    # Test case 8: Get users with invalid limit
    ("admin_token", "admin", "email", "asc", 1, 0, 200, True),
    # Test case 9: Get users with no search, sort_by, sort_order, page, limit
    ("admin_token", "", "", "", 0, 0, 200, True),
    # Test case 10: Get users with non-existing search
    ("admin_token", "non_existing", "email", "asc", 1, 2, 200, True),
]


@pytest.mark.parametrize("token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success", get_users_test_cases, ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], indirect=["token_fixture"])
def test_get_users(client, token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success):
    response = client.get(f"/api/admin/users?search={search_field}&sortBy={sort_by}&sortOrder={sort_order}&page={page}&limit={limit}", headers={
        "Authorization": f"Bearer {token_fixture}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success


delete_user_test_cases = [
    # Test case 1: Delete user with valid user_id
    ("admin_token", "complete_user_id", 200, True),

    # Test case 2: Delete user with non-existing user_id
    ("admin_token", 1000, 404, False),

    # Test case 3: Delete user with no token
    ("", "complete_user_id", 401, False),

    # Test case 4: Delete user with invalid token
    ("carrier_token", "complete_user_id", 401, False),

    # Test case 5: Delete self
    ("admin_token", "self", 403, False)
]


@pytest.mark.parametrize("token_fixture, user_id, expected_status_code, expected_success", delete_user_test_cases, ids=["1", "2", "3", "4", "5"], indirect=["token_fixture"])
def test_delete_user(client, token_fixture, user_id, expected_status_code, expected_success):
    if user_id == "self":
        user_id = db.session.query(User).filter_by(
            email=consts.ADMIN_EMAIL).first().user_id
    elif user_id == "complete_user_id":
        user_id = db.session.query(User).filter_by(
            email=consts.COMPLETE_USER_EMAIL).first().user_id

    response = client.delete(f"/api/admin/users/{user_id}", headers={
        "Authorization": f"Bearer {token_fixture}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success


def update_user(client, token, user_id, email, role_id, expected_status_code, expected_success):
    response = client.put(f"/api/admin/users/{user_id}", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={
        "email": email,
        "roleId": role_id
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success


def test_update_user(client, admin_token, carrier_token):
    # Test case 1: Update user with valid inputs
    update_user(client, admin_token, 1, "updated@gmail.com",
                "updated2", 2, 200, True)

    # Test case 2: Update user with non-existing user_id
    update_user(client, admin_token, 1000,
                "updated@gmail.com", "updated1", 1, 400, False)

    # Test case 3: Update user with invalid email
    update_user(client, admin_token, 1, consts.INVALID_EMAIL,
                "updated1", 1, 400, False)

    # Test case 4: Update user with invalid role_id
    update_user(client, admin_token, 1, "updated@gmail.com",
                "updated1", 100, 400, False)

    # Test case 5: Update user with no token
    update_user(client, "", 1, "updated@gmail.com", "updated1", 1, 401, False)

    # Test case 6: Update user with invalid token
    update_user(client, carrier_token, 1, "updated@gmail.com",
                "updated1", 1, 401, False)

    # Test case 7: No changes made
    complete_user_id = db.session.query(User).filter_by(
        email=consts.COMPLETE_USER_EMAIL).first().user_id
    update_user(client, admin_token, complete_user_id,
                consts.COMPLETE_USER_EMAIL, 1, 200, True)
