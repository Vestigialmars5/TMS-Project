
# test_admin.py
def test_create_user(client, auth_token):
    response = client.post("/api/admin/users", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={
        "email": "test@example.com",
        "password": "password",
        "roleId": 1
    })

    assert response.status_code == 201
    assert response.json["success"] == True


def test_get_users_plain(client, auth_token):
    response = client.get("/api/admin/users", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_get_users_complex(client, auth_token):
    response = client.get("/api/admin/users?search=admin&sortBy=username&sortOrder=desc&page=1&limit=2", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_delete_user(client, auth_token):
    response = client.delete("/api/admin/users/1", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200
    assert response.json["success"] == True


def test_update_user(client, auth_token):
    response = client.put("/api/admin/users/1", headers={
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }, json={
        "username": "new_username",
        "email": "new_email@example.com",
        "roleId": 2
    })

    assert response.status_code == 200
    assert response.json["success"] == True
