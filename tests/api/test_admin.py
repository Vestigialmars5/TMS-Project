from tests.utilstest import admin_token, carrier_token
from server.models.tms_models import User
from server.extensions import db
import tests.consts as consts


def test_create_user(client, admin_token):
    response = client.post("/api/admin/users", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={
        "email": consts.COMPLETE_USER_EMAIL,
        "password": consts.COMPLETE_USER_PASSWORD,
        "roleId": consts.COMPLETE_USER_ROLE_ID
    })

    assert response.status_code == 201
    assert response.json["success"] == True

    user = db.session.query(User).filter(
        User.email == consts.COMPLETE_USER_EMAIL).first()
    assert user is not None


def test_bad_create_user(client, admin_token):
    response = client.post("/api/admin/users", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={
        "email": consts.INVALID_EMAIL,
        "password": consts.COMPLETE_USER_PASSWORD,
        "roleId": 3
    })

    assert response.status_code == 401


def test_get_users_plain(client, admin_token):
    response = client.get("/api/admin/users", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_get_users_complex(client, admin_token):
    response = client.get("/api/admin/users?search=admin&sortBy=username&sortOrder=desc&page=1&limit=2", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_delete_user(client, admin_token):
    response = client.delete("/api/admin/users/1", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_update_user(client, admin_token):
    # Test case 1: Update user with valid inputs
    response = client.put("/api/admin/users/1", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={
        "username": "new_username",
        "email": "new_email@example.com",
        "roleId": 2
    })

    assert response.status_code == 200
    assert response.json["success"] == True

    # Test case 2: Update user with existing username
    # Test case 3: Update user with non-existing user_id
    # Test case 4: Update user with no changes made