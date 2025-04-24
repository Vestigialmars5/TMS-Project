from server.utils.validations import *
from server.utils.cleaners import *


def data_cleanup_login(data):
    email = clean_email(data.get("email"))
    password = data.get("password")

    if not is_password_valid(password):
        raise DataValidationError("Invalid Password")

    return email, password


def data_cleanup_onboarding_user_details(data):
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


def data_cleanup_customer(data):
    company_name = clean_company_name(data.get("companyName"))
    company_address = clean_address(data.get("companyAddress"))

    return company_name, company_address


def data_cleanup_create_user(data):
    email = clean_email(data.get("email"))
    password = data.get("password")
    role_id = clean_role_id(data.get("roleId"))

    if not is_password_valid(password):
        raise DataValidationError("Invalid Password")

    return email, password, role_id


def data_cleanup_search(args):
    search = clean_search(args.get("search"))
    page = clean_page(args.get("page"))
    limit = clean_limit(args.get("limit"))

    return search, page, limit

def data_cleanup_sort_users(args):
    sort_by = clean_sort_by_users(args.get("sortBy"))
    sort_order = clean_sort_order(args.get("sortOrder"))
    return sort_by, sort_order

def data_cleanup_sort_orders(args):
    sort_by = clean_sort_by_orders(args.get("sortBy"))
    sort_order = clean_sort_order(args.get("sortOrder"))

    return sort_by, sort_order


def data_cleanup_update_user(data):
    email = clean_email(data.get("email"))
    role_id = clean_role_id(data.get("roleId"))

    return email, role_id


def data_cleanup_create_order(data):
    reference_id = clean_reference_id(data.get("referenceId"))
    customer_id = clean_user_id(data.get("customerId"))
    delivery_address = clean_address(data.get("deliveryAddress"))
    order_products = clean_products(data.get("orderProducts"))
    return reference_id, customer_id, delivery_address, order_products


def data_cleanup_get_order_details(data):
    order_id = clean_order_id(data.get("orderId"))
    return order_id