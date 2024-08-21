from server.utils.validations import *
from server.utils.cleaners import *

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


def data_cleanup_get_users(args):
    search = clean_search(args.get("search"))
    sort_by = clean_sort_by(args.get("sortBy"))
    sort_order = clean_sort_order_users(args.get("sortOrder"))
    page = clean_page(args.get("page"))
    limit = clean_limit(args.get("limit"))

    return search, sort_by, sort_order, page, limit

