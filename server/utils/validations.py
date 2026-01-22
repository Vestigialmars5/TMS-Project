# Use validator class to validate data
from server.utils.cleaners import *
from server.extensions import db
from server.models.tms_models import *
from werkzeug.security import check_password_hash
from server.utils.exceptions import DatabaseQueryError
from server.utils.consts import MIN_PASSWORD


def user_exists(user_id=None, email=None):
    try:
        if user_id:
            return db.session.query(User).filter(User.user_id == user_id).first() is not None
        elif email:
            return db.session.query(User).filter(User.email == email).first() is not None
        else:
            return False
    except Exception as e:
        raise DatabaseQueryError("Error Finding User")


# Different from user_exists. I rather have two different functions
def get_user(user_id=None, email=None):
    try:
        if user_id:
            return db.session.query(User).filter(
                User.user_id == user_id).first()
        elif email:
            user = db.session.query(User).filter(User.email == email).first()
            return user
        else:
            return None
    except Exception as e:
        raise DatabaseQueryError("Error Getting User")


def get_order(order_id=None, reference_id=None):
    try:
        if order_id:
            return db.session.query(Order).filter(
                Order.order_id == order_id).first()
        elif reference_id:
            order = db.session.query(Order).filter(
                Order.reference_id == reference_id).first()
            return order
        else:
            return None
    except Exception as e:
        raise DatabaseQueryError("Error Getting Order")


def is_password_valid(password):
    if not password or not isinstance(password, str):
        return False
    return len(password) >= MIN_PASSWORD


def validate_login_credentials(email, password):
    user = get_user(email=email)

    if not user:
        return False

    # TODO: Uncomment -Ignores if password is wrong
    if not check_password_hash(user.password, password):
        return False

    return True


def validate_delete_user(user_id, initiator_id):
    if user_id == initiator_id:
        return False, "Cannot Delete Self"

    if not user_exists(user_id=user_id):
        return False, "User Does Not Exist"

    return True, ""


def validate_update_user(user_id, email, role_id, initiator_id):
    if user_id == initiator_id:
        return False, "Cannot Update Self"

    user = get_user(user_id=user_id)

    if not user:
        return False, "User Does Not Exist"

    if user.email == email and user.role_id == role_id:
        return False, "No Changes Made"

    return True, user


def order_exists(reference_id):
    try:
        return db.session.query(Order).filter(Order.order_uuid == reference_id).first() is not None
    except Exception as e:
        raise DatabaseQueryError("Error Finding Order")


# TODO: Uncomment when I add products to the db
def validate_order_products(products):

    try:
        total = 0
        for product in products:
            # product_details = db.session.query(Product).filter(Product.product_id == product["product_id"]).first()

            # if product_details is None:
            # return False, "Product Does Not Exist"

            # if product_details["product_name"] is None:
            # return False, "Product Name Missing"

            # if product_details["quantity"] <= 0:
            # return False, "Invalid Product Quantity"

            # if product_details["total_price"] <= 0:
            # return False, "Invalid Total Price"

            total += product["total_price"]

        return True, total
    except:
        raise DatabaseQueryError("Error Handling Product")


def validate_customer_update_order(reference_id, customer_id=None, delivery_address=None, order_products=None):

    ORDER_FIELD_PERMISSIONS = {
        "Pending": {"customer_id", "delivery_address", "order_products"},
        "Validated": {"delivery_address"},
        "Assigned": set()
    }

    
    if not order_exists(reference_id):
        return False, "Order Does Not Exist"

    order = get_order(reference_id=reference_id)

    allowed_fields = ORDER_FIELD_PERMISSIONS[order.status]

    changes = get_order_changes(order, customer_id, delivery_address, order_products)

    if not changes:
        return False, "No Changes Detected"
    
    disallowed_fields = set(changes.keys()) - allowed_fields
    if disallowed_fields:
        return False, f"Cannot Modify {', '.join(disallowed_fields)}"
    
    return True, {"order": order, "changes": changes}


def get_order_changes(order, customer_id, delivery_address, order_products):
    changes = {}

    if (customer_id is not None and order.customer_id != customer_id):
        changes["customer_id"] = customer_id
    
    if (delivery_address is not None and order.delivery_address != delivery_address):
        changes["delivery_address"] = delivery_address

    if order_products is not None:
        # get_product_changes(order_products)
        changes["order_products"] = order_products


    return changes


def get_product_changes(products):
    # TODO: Implement something that can check every product and compare it to the one stored in the db
    # It will probably have to go something like this
    # Get all order details with the reference id (that will return all the products linked to the order), then go one by one comparing each of the details.

    changes = []

    return changes
