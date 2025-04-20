import pytest
from server.extensions import db
from server.models.tms_models import User, UserDetails, Role
import tests.consts as consts
from werkzeug.security import generate_password_hash
import json


class TestUtils:
    """Utility functions for testing"""

    @staticmethod
    def assert_response_structure(response, expected_status, expected_success, expected_fields=None):
        """Helper method to check common response structure

        Args:
            response: Flask test client response
            expected_status: Expected HTTP status code
            expected_success: Expected success flag
            expected_fields: List of fields expected in the response data
        """
        assert response.status_code == expected_status
        assert response.json["success"] == expected_success

        if expected_fields and expected_success:
            for field in expected_fields:
                assert field in response.json, f"Expected field '{field}' missing from response"

    @staticmethod
    def login(client, email, password):
        """Perform login and return response

        Args:
            client: Flask test client
            email: User email
            password: User password
            
        Returns:
            Response object
        """
        return client.post("/api/auth/login", json={
            "email": email,
            "password": password
        })


@pytest.fixture()
def token_fixture(request):
    """Dynamic fixture that returns the requested token fixture"""
    print("hererererere")
    token_name = request.param
    if token_name == "":
        return ""
    
    hey = request.getfixturevalue(token_name)
    print(hey)
    return hey


@pytest.fixture()
def admin_token(client):
    """Get authentication token for admin user"""
    response = TestUtils.login(
        client, consts.ADMIN_EMAIL, consts.ADMIN_PASSWORD)
    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def customer_token(client):
    """Get authentication token for customer user"""
    response = TestUtils.login(
        client, consts.CUSTOMER_EMAIL, consts.CUSTOMER_PASSWORD)
    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def carrier_token(client):
    """Get authentication token for carrier user"""
    response = TestUtils.login(
        client, consts.CARRIER_EMAIL, consts.CARRIER_PASSWORD)
    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def user_complete_token(client):
    """Get authentication token for complete user"""
    response = TestUtils.login(
        client, consts.COMPLETE_USER_EMAIL, consts.COMPLETE_USER_PASSWORD)

    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def incomplete_user_token(client):
    """Get authentication token for incomplete user"""
    response = TestUtils.login(
        client, consts.INCOMPLETE_USER_EMAIL, consts.INCOMPLETE_USER_PASSWORD)
    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def incomplete_customer_token(client):
    """Get authentication token for incomplete customer"""
    response = TestUtils.login(
        client, consts.INCOMPLETE_CUSTOMER_EMAIL, consts.INCOMPLETE_CUSTOMER_PASSWORD)
    assert response.status_code == 200
    return response.json["accessToken"]


@pytest.fixture()
def get_user_id():
    """Factory fixture that returns a function to get a user ID by email"""
    def _get_user_id(email):
        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            return None
        return user.user_id
    return _get_user_id


@pytest.fixture()
def get_role_name():
    def _get_role_name(role_id):
        role_name = db.session.query(Role).filter_by(role_id=role_id).first().role_name
        if not role_name:
            return None
        return role_name
    return _get_role_name


@pytest.fixture()
def auth_headers():
    """Factory fixture that returns a function to create authorization headers"""
    def _make_headers(token):
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    return _make_headers
