from tests.utilstest import incomplete_user_token, incomplete_customer_token, TestUtils, auth_headers, get_role_name
import pytest
from tests.utilstest import token_fixture
import tests.consts as consts



class TestOnboarding:
    """ Test cases for onboarding functionality """

    # Onboarding Step 1
    @pytest.mark.parametrize(
        "token_fixture, email, password, confirmation, first_name, last_name, phone_number, address, role_id, role_name, expected_status_code, expected_success",
        [
            # Valid request
            ("incomplete_user_token", consts.INCOMPLETE_USER_EMAIL, consts.INCOMPLETE_USER_PASSWORD, consts.INCOMPLETE_USER_PASSWORD,
             consts.INCOMPLETE_USER_FIRST_NAME, consts.INCOMPLETE_USER_LAST_NAME,
             consts.INCOMPLETE_USER_PHONE_NUMBER, consts.INCOMPLETE_USER_ADDRESS, consts.INCOMPLETE_USER_ROLE_ID, "valid", 200, True),
        ],
        ids=[
            "valid_request"
        ],
        indirect=["token_fixture"])
    def test_onboard_user(self, client, token_fixture, email, password, confirmation, first_name, last_name, phone_number, address, role_id, role_name, expected_status_code, expected_success, get_role_name, auth_headers):
        """ Test onboarding a user (step 1) with various inputs """

        if role_name == "valid":
            role_name = get_role_name(role_id)

        headers = auth_headers(token_fixture)

        response = client.post("/api/onboarding/details", headers=headers, json={
            "email": email,
            "password": password,
            "confirmation": confirmation,
            "firstName": first_name,
            "lastName": last_name,
            "phoneNumber": phone_number,
            "address": address,
            "role_id": role_id,
            "role_name": role_name
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success
        )

    @pytest.mark.parametrize(
        "token_fixture, role_id, company_name, company_address, expected_status_code, expected_success",
        [
            # Valid request
            ("incomplete_customer_token", consts.INCOMPLETE_CUSTOMER_ROLE_ID,
             consts.INCOMPLETE_CUSTOMER_COMPANY_NAME, consts.INCOMPLETE_CUSTOMER_COMPANY_ADDRESS, 200, True),
        ],
        ids=[
            "valid_request"
        ],
        indirect=["token_fixture"])
    def test_onboard_customer(self, client, token_fixture, role_id, company_name, company_address, expected_status_code, expected_success, auth_headers):
        """ Test onboarding a user with customer role with various inputs """

        headers = auth_headers(token_fixture)

        response = client.post("/api/onboarding/4", headers=headers, json={
            "roleId": role_id,
            "companyName": company_name,
            "companyAddress": company_address
        })

        TestUtils.assert_response_structure(
            response,
            expected_status_code,
            expected_success
        )
