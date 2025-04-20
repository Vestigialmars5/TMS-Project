import pytest
from server.models.tms_models import User, UserDetails
from tests.utilstest import token_fixture, TestUtils, admin_token, carrier_token, auth_headers, get_user_id
from server.extensions import db
import tests.consts as consts
import json


class TestUserManagement:
    """Test cases for user management functionality"""

    @pytest.mark.parametrize(
        "token_fixture, email, password, role_id, expected_status_code, expected_success",
        [
            # Valid creation
            ("admin_token", "new@gmail.com", "newnewnew", 1, 201, True),
            # Email already exists
            ("admin_token", consts.ADMIN_EMAIL,
             consts.ADMIN_PASSWORD, consts.ADMIN_ROLE_ID, 409, False),
            # Invalid email format
            ("admin_token", consts.INVALID_EMAIL, "password", 1, 400, False),
            # Invalid password (too short)
            ("admin_token", "new@gmail.com", "short", 1, 400, False),
            # Invalid role_id
            ("admin_token", "new@gmail.com", "newnewnew", 100, 400, False),
            # Missing all fields
            ("admin_token", "", "", 0, 400, False),
            # Missing email
            ("admin_token", "", "password", 1, 400, False),
            # Missing password
            ("admin_token", "new@gmail.com", "", 1, 400, False),
            # Missing role_id
            ("admin_token", "new@gmail.com", "newnewnew", 0, 400, False),
            # No authorization
            ("", "new@gmail.com", "newnewnew", 1, 401, False),
            # Unauthorized role (carrier)
            ("carrier_token", "new@gmail.com", "newnewnew", 1, 401, False)
        ],
        ids=[
            "valid_creation",
            "duplicate_email",
            "invalid_email_format",
            "invalid_password",
            "invalid_role_id",
            "missing_all_fields",
            "missing_email",
            "missing_password",
            "missing_role_id",
            "no_authorization",
            "unauthorized_role"
        ],
        indirect=["token_fixture"]
    )
    def test_create_user(self, client, token_fixture, email, password, role_id,
                         expected_status_code, expected_success, auth_headers):
        """Test creating new users with various inputs and validations."""

        headers = auth_headers(token_fixture)

        response = client.post("/api/users", headers=headers, json={
            "email": email,
            "password": password,
            "roleId": role_id
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success
        )

    @pytest.mark.parametrize(
        "token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success",
        [
            # Valid request
            ("admin_token", "admin", "email", "asc", 1, 2, 200, True),
            # No authorization
            ("", "admin", "email", "asc", 1, 2, 401, False),
            # Unauthorized role
            ("carrier_token", "admin", "email", "asc", 1, 2, 401, False),
            # Non-string search (should still work)
            ("admin_token", 1, "email", "asc", 1, 2, 200, True),
            # Invalid sort_by field
            ("admin_token", "admin", "invalid_sort_by", "asc", 1, 2, 200, True),
            # Invalid sort_order
            ("admin_token", "admin", "email",
             "invalid_sort_order", 1, 2, 200, True),
            # Invalid page number
            ("admin_token", "admin", "email", "asc", 0, 2, 200, True),
            # Invalid limit
            ("admin_token", "admin", "email", "asc", 1, 0, 200, True),
            # Empty parameters
            ("admin_token", "", "", "", 0, 0, 200, True),
            # Non-matching search
            ("admin_token", "non_existing", "email", "asc", 1, 2, 200, True),
        ],
        ids=[
            "valid_request",
            "no_authorization",
            "unauthorized_role",
            "non_string_search",
            "invalid_sort_by",
            "invalid_sort_order",
            "invalid_page",
            "invalid_limit",
            "empty_parameters",
            "non_matching_search"
        ],
        indirect=["token_fixture"]
    )
    def test_get_users(self, client, token_fixture, search_field, sort_by, sort_order, page, limit, expected_status_code, expected_success, auth_headers):
        """Test retrieving users with various filtering and sorting options"""

        headers = auth_headers(token_fixture)

        response = client.get(f"/api/users?search={search_field}&sortBy={sort_by}&sortOrder={sort_order}&page={page}&limit={limit}", headers=headers, json={})
        print(response, "resssponse")

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
            expected_fields=["users"] if expected_success else None
        )

    @pytest.mark.parametrize(
        "token_fixture, user_id, expected_status_code, expected_success",
        [
            # Valid request
            ("admin_token", "complete_user_id", 200, True),
            # Invalid user_id (non-existing)
            ("admin_token", 1000, 404, False),
            # No authorization
            ("", "complete_user_id", 401, False),
            # Unauthorized role
            ("carrier_token", "complete_user_id", 401, False),
            # Invalid action (deleting self)
            ("admin_token", "self", 403, False)
        ],
        ids=[
            "valid_request",
            "invalid_user_id",
            "no_authorization",
            "unauthorized_role",
            "invalid_action"
        ], indirect=["token_fixture"])
    def test_delete_user(self, client, token_fixture, user_id, expected_status_code, expected_success, get_user_id, auth_headers):
        """Test deleting users with various inputs"""

        if user_id == "self":
            user_id = get_user_id(consts.ADMIN_EMAIL)
        elif user_id == "complete_user_id":
            user_id = get_user_id(consts.COMPLETE_USER_EMAIL)

        headers = auth_headers(token_fixture)
        response = client.delete(f"/api/users/{user_id}", headers=headers, json={})

        assert response.status_code == expected_status_code
        assert response.json["success"] == expected_success
        if response.json["success"]:
            assert db.session.query(User).filter_by(
                user_id=user_id).first() is None
            assert db.session.query(UserDetails).filter_by(
                user_id=user_id).first() is None

    @pytest.mark.parametrize(
        "token_fixture, user_id, email, role_id, expected_status_code, expected_success",
        [
            # Valid request
            ("admin_token", "complete_user_id", "updated@gmail.com", 2, 200, True),
            # Invalid user_id (non-existing)
            ("admin_token", 1000, "updated@gmail.com", 1, 404, False),
            # Invalid email format
            ("admin_token", "complete_user_id",
             consts.INVALID_EMAIL, 1, 400, False),
            # Invalid role_id
            ("admin_token", "complete_user_id",
             "updated@gmail.com", 100, 400, False),
            # No authorization
            ("", "complete_user_id", "updated@gmail.com", 1, 401, False),
            # Unauthorized role
            ("carrier_token", "complete_user_id",
             "updated@gmail.com", 1, 401, False),
            # No changes made
            ("admin_token", "complete_user_id", consts.COMPLETE_USER_EMAIL,
             consts.COMPLETE_USER_ROLE_ID, 200, True)
        ],
        ids=[
            "valid_request",
            "invalid_user_id",
            "invalid_email_format",
            "invalid_role_id",
            "no_authorization",
            "unauthorized_role",
            "no_changes_made"
        ], indirect=["token_fixture"])
    def test_update_user(self, client, token_fixture, user_id, email, role_id, expected_status_code, expected_success, get_user_id, auth_headers):
        """Test updating users with various inputs"""

        if user_id == "complete_user_id":
            user_id = get_user_id(consts.COMPLETE_USER_EMAIL)

        headers = auth_headers(token_fixture)

        response = client.put(f"/api/users/{user_id}", headers=headers, json={
            "email": email,
            "roleId": role_id
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
        )

    @pytest.mark.parametrize(
        "token_fixture, expected_status_code, expected_success",
        [
            # Valid request
            ("admin_token", 200, True),
            # No authorization
            ("", 401, False)
        ],
        ids=[
            "valid_request",
            "no_authorization"
        ], indirect=["token_fixture"])
    def test_get_roles(self, client, token_fixture, expected_status_code, expected_success, auth_headers):
        """Test retrieving roles with various inputs"""

        headers = auth_headers(token_fixture)

        response = client.get("/api/roles", headers=headers, json={})

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success,
        )
