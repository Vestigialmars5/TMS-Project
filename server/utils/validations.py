# Use validator class to validate data
from server.utils.cleaners import *
from server.extensions import db
from server.models.tms_models import *
from werkzeug.security import check_password_hash
from server.utils.exceptions import DatabaseQueryError
from server.utils.helpers import create_unique_username


def user_exists(user_id=None, email=None, username=None):
    try:
        if user_id:
            return db.session.query(User).filter(User.user_id == user_id).first() is not None
        elif email:
            return db.session.query(User).filter(User.email == email).first() is not None
        elif username:
            return db.session.query(User).filter(User.username == username).first() is not None
        else:
            return False
    except Exception as e:
        raise DatabaseQueryError("Error Finding User")


# Different from user_exists. I rather have two different functions
def get_user(user_id=None, email=None, username=None):
    try:
        if user_id:
            return db.session.query(User).filter(
                User.user_id == user_id).first()
        elif email:
            return db.session.query(User).filter(User.email == email).first()
        elif username:
            return db.session.query(User).filter(
                User.username == username).first()
        else:
            return None
    except Exception as e:
        raise DatabaseQueryError("Error Getting User")

def is_password_valid(password):
    if not password or not isinstance(password, str):
        return False
    return len(password) >= MIN_PASSWORD


def validate_login_credentials(email, password):
    if not user_exists(email=email):
        return False

    # TODO: Uncomment -Ignores if password is wrong
    """ if not check_password_hash(user.password, password):
        return False """

    return True


def validate_delete_user(user_id, initiator_id):
    if user_id == initiator_id:
        return False, "Cannot Delete Self"

    if not user_exists(user_id=user_id):
        return False, "User Does Not Exist"

    return True


def validate_update_user(user_id, username, email, role_id):
    user = get_user(user_id=user_id)

    if not user:
        return False, "User Does Not Exist"

    if user.username == username and user.email == email and user.role_id == role_id:
        return False, "No Changes Made"

    if user_exists(username=username):
        recommended = create_unique_username(username)
        return False, "Username Already Exists: Recommended {recommended}"

    return True
