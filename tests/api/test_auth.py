import tests.consts as consts
from tests.utilstest import admin_token, TestUtils, auth_headers, token_fixture
import pytest


class TestAuth:
    """Test cases for authentication endpoints"""

    @pytest.mark.parametrize(
        "email, password, expected_status_code, expected_success",
        [
            # Valid login
            (consts.ADMIN_EMAIL, consts.ADMIN_PASSWORD, 200, True),
            # Invalid email format
            (consts.INVALID_EMAIL, consts.ADMIN_PASSWORD, 400, False),
            # Invalid password format (too short)
            (consts.ADMIN_EMAIL, consts.INVALID_PASSWORD, 400, False),
            # Missing credentials
            ("", "", 400, False),
            # Incorrect password
            (consts.ADMIN_EMAIL, consts.CARRIER_PASSWORD, 401, False),
            # Non-existent user
            ("i_dont_exist@gmail.com", consts.ADMIN_PASSWORD, 401, False)
        ],
        ids=[
            "valid_login",
            "invalid_email_format",
            "invalid_password_format",
            "missing_credentials",
            "incorrect_password", 
            "non_existent_user"
        ]
    )
    def test_login(self, client, email, password, expected_status_code, expected_success):
        """Test the login endpoint with various inputs"""
        response = TestUtils.login(client, email, password)

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
        )

    @pytest.mark.parametrize(
        "token_fixture, expected_status_code, expected_success",
        [
            # Valid logout
            ("admin_token", 200, True),
            # No authorization header
            ("", 401, False),
        ],
        ids=[
            "valid_logout",
            "no_authorization_header"
        ], indirect=["token_fixture"]
    )
    def test_logout(self, client, token_fixture, expected_status_code, expected_success, auth_headers):
        """Test logout functionality"""

        headers = auth_headers(token_fixture)

        response = client.post("/api/auth/logout", headers=headers, json={})

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
        )
