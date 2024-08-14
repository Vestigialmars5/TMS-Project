from tests.utilstest import admin_token

def test_login(client):
    response = client.post("/api/auth/login", json={
        "email": "admin@gmail.com",
        "password": "asdfasdf"
    })

    assert response.status_code == 200
    assert response.json["success"] == True
    assert "access_token" in response.json


def test_logout(client, admin_token):
    response = client.post("api/auth/logout", headers={
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }, json={})

    assert response.status_code == 200


def test_bad_login(client):
    response = client.post("/api/auth/login", json={
        "email": "admin@wrong.com",
        "password": "wrong"
    })

    assert response.status_code == 401
    assert response.json["success"] == False
    assert response.json["error"] == "Invalid Credentials"