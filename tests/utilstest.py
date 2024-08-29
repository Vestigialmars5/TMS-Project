import pytest
from server.extensions import db
from server.models.tms_models import User, UserDetails
import tests.consts as consts


@pytest.fixture()
def admin_token(client):
    user = User(
        email=consts.ADMIN_EMAIL,
        username=consts.ADMIN_USERNAME,
        password=consts.ADMIN_PASSWORD,
        role_id=consts.ADMIN_ROLE_ID
    )
    db.session.add(user)
    db.session.commit()

    user_details = UserDetails(
        user_id=user.user_id,
        first_name=consts.ADMIN_FIRST_NAME,
        last_name=consts.ADMIN_LAST_NAME,
        phone_number=consts.ADMIN_PHONE_NUMBER,
        address=consts.ADMIN_ADDRESS
    )

    assert db.session.query(User).filter_by(email=consts.ADMIN_EMAIL).first() is not None

    response = client.post("api/auth/login", json={
        "email": consts.ADMIN_EMAIL,
        "password": consts.ADMIN_PASSWORD
    })
    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def carrier_token(client):
    user = User(
        email=consts.CARRIER_EMAIL,
        username=consts.CARRIER_USERNAME,
        password=consts.CARRIER_PASSWORD,
        role_id=consts.CARRIER_ROLE_ID
    )
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).filter_by(email=consts.CARRIER_EMAIL).first() is not None

    user_details = UserDetails(
        user_id=user.user_id,
        first_name=consts.CARRIER_FIRST_NAME,
        last_name=consts.CARRIER_LAST_NAME,
        phone_number=consts.CARRIER_PHONE_NUMBER,
        address=consts.CARRIER_ADDRESS
    )

    db.session.add(user_details)   
    db.session.commit()

    assert db.session.query(UserDetails).filter_by(user_id=user.user_id).first() is not None

    response = client.post("api/auth/login", json={
        "email": consts.CARRIER_EMAIL,
        "password": consts.CARRIER_PASSWORD
    })

    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def user_complete_token(client):
    user = User(
        email="test_user_complete@email.com",
        username="test_user_complete",
        password="asdfasdf",
        role_id=1
    )
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).filter_by(email="test_user_complete@email.com").first() is not None

    user_details = UserDetails(
        user_id=user.user_id,
        first_name="Test",
        last_name="User",
        phone_number="1234567890",
        address="123 Test St."
    )
    db.session.add(user_details)
    db.session.commit()

    assert db.session.query(UserDetails).filter_by(user_id=user.user_id).first() is not None

    response = client.post("api/auth/login", json={
        "email": "test_user_complete@email.com",
        "password": "asdfasdf"
    })

    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def user_not_onboarded_token(client):
    user = User(
        email="test_user_not_onboarded@email.com",
        username="test_user_not_onboarded",
        password="asdfasdf",
        role_id=1
    )
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).filter_by(email="test_user_not_onboarded@email.com").first() is not None

    response = client.post("api/auth/login", json={
        "email": "test_user_not_onboarded@email.com",
        "password": "asdfasdf"
    })

    assert response.status_code == 200
    return response.json["access_token"]
