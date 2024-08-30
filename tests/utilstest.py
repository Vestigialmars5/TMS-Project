import pytest
from server.extensions import db
from server.models.tms_models import User, UserDetails
import tests.consts as consts
from werkzeug.security import generate_password_hash


@pytest.fixture()
def admin_token(client):
    hashed_password = generate_password_hash(consts.ADMIN_PASSWORD)

    user = User(
        email=consts.ADMIN_EMAIL,
        username=consts.ADMIN_USERNAME,
        password=hashed_password,
        role_id=consts.ADMIN_ROLE_ID,
        status=consts.ADMIN_STATUS
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

    db.session.add(user_details)
    db.session.commit()

    assert db.session.query(User).filter_by(email=consts.ADMIN_EMAIL).first() is not None

    response = client.post("api/auth/login", json={
        "email": consts.ADMIN_EMAIL,
        "password": consts.ADMIN_PASSWORD
    })
    assert response.status_code == 200
    return response.json["access_token"]


@pytest.fixture()
def carrier_token(client):
    hashed_password = generate_password_hash(consts.CARRIER_PASSWORD)

    user = User(
        email=consts.CARRIER_EMAIL,
        username=consts.CARRIER_USERNAME,
        password=hashed_password,
        role_id=consts.CARRIER_ROLE_ID,
        status=consts.CARRIER_STATUS
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
    hashed_password = generate_password_hash(consts.COMPLETE_USER_PASSWORD)
    user = User(
        email=consts.COMPLETE_USER_EMAIL,
        username=consts.COMPLETE_USER_USERNAME,
        password=hashed_password,
        role_id=consts.COMPLETE_USER_ROLE_ID,
        status=consts.COMPLETE_USER_STATUS
    )
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).filter_by(email="test_user_complete@email.com").first() is not None

    user_details = UserDetails(
        user_id=user.user_id,
        first_name=consts.COMPLETE_USER_FIRST_NAME,
        last_name=consts.COMPLETE_USER_LAST_NAME,
        phone_number=consts.COMPLETE_USER_PHONE_NUMBER,
        address=consts.COMPLETE_USER_ADDRESS
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
def incomplete_user_token(client):
    hashed_password = generate_password_hash(consts.INCOMPLETE_USER_PASSWORD)

    user = User(
        email=consts.INCOMPLETE_USER_EMAIL,
        username=consts.INCOMPLETE_USER_USERNAME,
        password=hashed_password,
        role_id=consts.INCOMPLETE_USER_ROLE_ID,
        status=consts.INCOMPLETE_USER_STATUS
    )
    db.session.add(user)
    db.session.commit()

    assert db.session.query(User).filter_by(email=consts.INCOMPLETE_USER_EMAIL).first() is not None

    response = client.post("api/auth/login", json={
        "email": consts.INCOMPLETE_USER_EMAIL,
        "password": consts.INCOMPLETE_USER_PASSWORD
    })

    assert response.status_code == 200
    return response.json["access_token"]
