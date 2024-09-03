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

def is_password_valid(password):
    if not password or not isinstance(password, str):
        return False
    return len(password) >= MIN_PASSWORD


def validate_login_credentials(email, password):
    user = get_user(email=email)

    if not user:
        return False

    print(user, password)
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


def validate_update_user(user_id, email, role_id):
    user = get_user(user_id=user_id)

    if not user:
        return False, "User Does Not Exist"

    if user.email == email and user.role_id == role_id:
        return False, "No Changes Made"

    return True, user
