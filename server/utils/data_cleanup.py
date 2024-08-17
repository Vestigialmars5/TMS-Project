from server.utils.validations import *

def data_cleanup_login(data):
    email = clean_email(data.get("email"))
    password = data.get("password")

    if not is_password_valid(password):
        raise DataValidationError("Invalid Password")

    return email, password


def data_cleanup_onboarding(data):
    password = data.get("password")
    confirmation = data.get("confirmation")

    if not is_password_valid(password) or not is_password_valid(confirmation):
        raise DataValidationError("Invalid Password")

    email = clean_email(data.get("email"))
    first_name = clean_name(data.get("firstName"))
    last_name = clean_name(data.get("lastName"))
    phone_number = clean_phone_number(data.get("phoneNumber"))
    address = clean_address(data.get("address"))

    return email, password, confirmation, first_name, last_name, phone_number, address


def data_cleanup_create_user(data):
    email = clean_email(data.get("email"))
    password = data.get("password")
    role_id = clean_role_id(data.get("roleId"))

    if not is_password_valid(password):
        raise DataValidationError("Invalid Password")

    return email, password, role_id