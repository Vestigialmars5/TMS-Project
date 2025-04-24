import re
import uuid
from server.utils.exceptions import DataValidationError
from server.utils.consts import MIN_NAME, MAX_NAME


def clean_email(email):
    if not email or not isinstance(email, str):
        raise DataValidationError("Email Missing or Invalid")

    # Email contains @ and .
    regex = r'[^@]+@[^@]+\.[^@]+'
    email = email.strip().lower()

    if not re.match(regex, email):
        raise DataValidationError("Invalid Email")

    return email


def clean_name(name):
    if not name or not isinstance(name, str):
        raise DataValidationError("Invalid Name")

    name = name.strip().title()
    if not MIN_NAME <= len(name) <= MAX_NAME:
        raise DataValidationError("Invalid Name")

    # Check if name contains only alphabets
    if not name.isalpha():
        raise DataValidationError("Invalid Name")

    return name


def clean_company_name(company_name):
    if not company_name or not isinstance(company_name, str):
        raise DataValidationError("Company Name Missing or Invalid")

    company_name = company_name.strip().title()

    return company_name


def clean_phone_number(phone_number):
    if not phone_number or not isinstance(phone_number, str):
        raise DataValidationError("Phone Number Missing or Invalid")
    # Remove all non-digits except '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    if not len(phone_number) == 10:
        if not phone_number.startswith('+') or not len(phone_number) == 12:
            raise DataValidationError("Invalid Phone Number Length")
        else:
            return phone_number
    else:
        return phone_number


def clean_address(address):
    # TODO: Implement address validation service
    if not address or not isinstance(address, str):
        raise DataValidationError("Address Missing or Invalid")

    address = address.strip()

    if 0 >= len(address) < 10:
        raise DataValidationError("Address Length Invalid")

    return address


def clean_user_id(user_id):
    if not user_id or not isinstance(user_id, int):
        raise DataValidationError("Missing Or Invalid User ID")

    if 0 >= user_id:
        raise DataValidationError("Invalid User ID")

    return user_id


def clean_role_id(role_id):
    if not role_id or not isinstance(role_id, int):
        raise DataValidationError("Role ID Missing or Invalid")

    # Role ID must be between 1 and 7
    if not 0 < role_id <= 7:
        raise DataValidationError("Invalid Role ID")

    return role_id


def clean_search(search):
    if not search or not isinstance(search, str):
        return ""

    return search.strip()


def clean_sort_order(sort_by):
    if not sort_by or not isinstance(sort_by, str):
        return "asc"

    sort_by = sort_by.strip().lower()

    if sort_by not in ["asc", "desc"]:
        return "asc"

    return sort_by


def clean_sort_by_users(sort_order):
    if not sort_order or not isinstance(sort_order, str):
        return "email"

    sort_order = sort_order.strip().lower()

    if sort_order not in ["email", "role_name"]:
        return "email"

    return sort_order


def clean_sort_by_orders(sort_order):
    if not sort_order or not isinstance(sort_order, str):
        return "status"

    sort_order = sort_order.strip().lower()

    if sort_order not in ["status"]:
        return "status"

    return sort_order



def clean_page(page):
    if not page or not isinstance(page, int):
        return 1

    return page


def clean_limit(limit):
    if not limit or not isinstance(limit, int):
        return 25

    if 0 >= limit > 100:
        return 25

    return limit


def clean_products(products):
    if not products or not isinstance(products, list) or len(products) == 0:
        raise DataValidationError("Product List Missing or Invalid")
    
    clean_products_list = []

    for product in products:
        clean_products_list.append(clean_product(product))
    
    return clean_products_list
    
def clean_product(product):
    if not product or not isinstance(product, dict):
        raise DataValidationError("Product Missing or Invalid")
    
    if "productId" not in product or not isinstance(product["productId"], int) or product["productId"] <= 0:
        raise DataValidationError("Product Id Missing or Invalid")

    if "productName" not in product or not isinstance(product["productName"], str):
        raise DataValidationError("Product Name Missing or Invalid")
    
    if "quantity" not in product or not isinstance(product["quantity"], int) or product["quantity"] <= 0:
        raise DataValidationError("Product Quantity Missing or Invalid")


    if "totalPrice" not in product or not isinstance(product["totalPrice"], float) or product["totalPrice"] <= 0:
        raise DataValidationError("Product Total Price Missing or Invalid")

    clean = {"product_id": product["productId"], "product_name": product["productName"], "quantity":product["quantity"], "total_price":product["totalPrice"]}
    
    return clean

def clean_reference_id(reference_id):
    if not reference_id or not isinstance(reference_id, str):
        raise DataValidationError("Reference Id Missing or Invalid")

    reference_id = reference_id.strip()

    try:
        uuid_obj = uuid.UUID(reference_id, version=4)
        if str(uuid_obj.version) != "4":
            raise DataValidationError("Invalid UUID Version")
    except ValueError:
        raise DataValidationError("Invalid UUId Format For Reference Id")
    
    return reference_id


def clean_order_id(order_id):
    if not order_id:
        raise DataValidationError("Order Id Missing")
    
    if isinstance(order_id, str):
        try:
            order_id = int(order_id)
        except ValueError:
            raise DataValidationError("Order Id Invalid")
    
    if order_id <= 0:
        raise DataValidationError("Order Id Invalid")
    
    return order_id
