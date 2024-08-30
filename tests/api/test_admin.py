from tests.utilstest import admin_token, carrier_token
from server.models.tms_models import User
from server.extensions import db
import tests.consts as consts


def create_user(client, token, email, password, role_id, expected_status_code, expected_success):
    response = client.post("/api/admin/users", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={
        "email": email,
        "password": password,
        "roleId": role_id
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success

    return response


def test_create_user(client, admin_token, carrier_token):
    # Test case 1: Create user with valid inputs
    create_user(client, admin_token, "new@gmail.com",
                "newnewnew", 1, 201, True)

    # Test case 2: Create user with existing email
    create_user(client, admin_token, consts.ADMIN_EMAIL,
                consts.ADMIN_PASSWORD, consts.ADMIN_ROLE_ID, 409, True)

    # Test case 3: Create user with invalid email
    create_user(client, admin_token, "invalid_email",
                "password", 1, 400, False)

    # Test case 4: Create user with invalid password
    create_user(client, admin_token, "new@gmail.com", "short", 1, 400, False)

    # Test case 5: Create user with invalid role_id
    create_user(client, admin_token, "new@gmail.com",
                "newnewnew", 100, 400, False)

    # Test case 6: Create user with no inputs
    create_user(client, admin_token, "", "", 0, 400, False)

    # Test case 7: Create user with no email
    create_user(client, admin_token, "", "password", 1, 400, False)

    # Test case 8: Create user with no password
    create_user(client, admin_token, "new@gmail.com", "", 1, 400, False)

    # Test case 9: Create user with no role_id
    create_user(client, admin_token, "new@gmail.com",
                "newnewnew", 0, 400, False)

    # Test case 10: Create user with no token
    create_user(client, "", "new@gmail.com", "newnewnew", 1, 401, False)

    # Test case 11: Create user with invalid token
    create_user(client, carrier_token, "new@gmail.com",
                "newnewnew", 1, 401, False)


def get_users(client, token, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success):
    response = client.get(f"/api/admin/users?search={search_field}&sortBy={sort_by}&sortOrder={sort_order}&page={page}&limit={limit}", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success

    return response


def test_get_users(client, admin_token, carrier_token):
    # Test case 1: Get users with valid inputs
    get_users(client, admin_token, "admin", "username", "asc", 1, 2, 200, True)

    # Test case 2: Get users with no token
    get_users(client, "", "admin", "username", "asc", 1, 2, 401, False)

    # Test case 3: Get users with invalid token
    get_users(client, carrier_token, "admin", "username", "asc", 1, 2, 401, False)

    # Test case 4: Get users with invalid search
    get_users(client, admin_token, "invalid_search", "username", "asc", 1, 2, 400, False)

    # Test case 5: Get users with invalid sort_by
    get_users(client, admin_token, "admin", "invalid_sort_by", "asc", 1, 2, 400, False)

    # Test case 6: Get users with invalid sort_order
    get_users(client, admin_token, "admin", "username", "invalid_sort_order", 1, 2, 400, False)

    # Test case 7: Get users with invalid page
    get_users(client, admin_token, "admin", "username", "asc", 0, 2, 400, False)

    # Test case 8: Get users with invalid limit
    get_users(client, admin_token, "admin", "username", "asc", 1, 0, 400, False)

    # Test case 9: Get users with no search, sort_by, sort_order, page, limit
    get_users(client, admin_token, "", "", "", 1, 2, 200, True)


def delete_user(client, token, user_id, expected_status_code, expected_success):
    response = client.delete(f"/api/admin/users/{user_id}", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success

    return response


def test_delete_user(client, admin_token, carrier_token):
    # Test case 1: Delete user with valid user_id
    delete_user(client, admin_token, 1, 200, True)

    # Test case 2: Delete user with non-existing user_id
    delete_user(client, admin_token, 1000, 400, False)

    # Test case 3: Delete user with no token
    delete_user(client, "", 1, 401, False)

    # Test case 4: Delete user with invalid token
    delete_user(client, carrier_token, 1, 401, False)

    # Test case 5: Delete self
    admin_id = db.session.query(User).filter_by(email=consts.ADMIN_EMAIL).first().user_id
    delete_user(client, admin_token, admin_id, 403, False)


def update_user(client, token, user_id, email, username, role_id, expected_status_code, expected_success):
    response = client.put(f"/api/admin/users/{user_id}", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, json={
        "email": email,
        "username": username,
        "roleId": role_id
    })

    assert response.status_code == expected_status_code
    assert response.json["success"] == expected_success

    return response


def test_update_user(client, admin_token, carrier_token):
    # Test case 1: Update user with valid inputs
    update_user(client, admin_token, 1, "updated@gmail.com", "updated2", 2, 200, True)
    
    # Test case 2: Update user with non-existing user_id
    update_user(client, admin_token, 1000, "updated@gmail.com", "updated1", 1, 400, False)

    # Test case 3: Update user with invalid email
    update_user(client, admin_token, 1, "invalid_email", "updated1", 1, 400, False)

    # Test case 4: Update user with invalid username
    update_user(client, admin_token, 1, "updated@gmail.com", "", 1, 400, False)

    # Test case 5: Update user with invalid role_id
    update_user(client, admin_token, 1, "updated@gmail.com", "updated1", 100, 400, False)

    # Test case 6: Update user with no token
    update_user(client, "", 1, "updated@gmail.com", "updated1", 1, 401, False)

    # Test case 7: Update user with invalid token
    update_user(client, carrier_token, 1, "updated@gmail.com", "updated1", 1, 401, False)

    # Test case 8: No changes made
    complete_user_id = db.session.query(User).filter_by(email=consts.COMPLETE_USER_EMAIL).first().user_id
    update_user(client, admin_token, complete_user_id, consts.COMPLETE_USER_EMAIL, consts.COMPLETE_USER_USERNAME, 1, 200, True)