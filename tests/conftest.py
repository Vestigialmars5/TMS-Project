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
        # Creates roles and admin
        populate_db(testing=True)
        yield app
        
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
