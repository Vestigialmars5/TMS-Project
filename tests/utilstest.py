import pytest
from server.extensions import db
from server.models.tms_models import User, UserDetails
import tests.consts as consts
from werkzeug.security import generate_password_hash


@pytest.fixture()
def token_fixture(request):
    token_name = request.param
    if token_name == "":
        return ""
    
    return request.getfixturevalue(token_name)

@pytest.fixture()
def admin_token(client):
    response = client.post("api/auth/login", json={
        "email": consts.ADMIN_EMAIL,
        "password": consts.ADMIN_PASSWORD
    })
    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def carrier_token(client):
    response = client.post("api/auth/login", json={
        "email": consts.CARRIER_EMAIL,
        "password": consts.CARRIER_PASSWORD
    })

    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def user_complete_token(client):
    response = client.post("api/auth/login", json={
        "email": "test_user_complete@email.com",
        "password": "asdfasdf"
    })

    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def incomplete_user_token(client):
    response = client.post("api/auth/login", json={
        "email": consts.INCOMPLETE_USER_EMAIL,
        "password": consts.INCOMPLETE_USER_PASSWORD
    })

    assert response.status_code == 200
    return response.json["access_token"]
