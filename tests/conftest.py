import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pytest
from server import create_app
from server.config import Testing
from server.extensions import db
from server.models import base
from server.db_initiator import init_db, populate_db



@pytest.fixture()
def app():
    app = create_app(Testing)

    with app.app_context():
        from server.models import tms_models
        from server.models import wms_models
        init_db()
        populate_db()
        yield app
        
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def auth_token(client):
    response = client.post("api/auth/login", json={
        "email": "asdf@asdf.com",
        "password": "asdfasdf"
    })
    assert response.status_code == 200
    print(f"The auth_token: {response.json["access_token"]}")
    return response.json["access_token"]