# Use validator class to validate data
from server.utils.cleaners import *
from server.extensions import db
from server.models.tms_models import *
from werkzeug.security import check_password_hash
from server.utils.exceptions import DatabaseQueryError


def user_exists(user_id=None, email=None, username=None):
    try:
        if user_id:
            user = db.session.query(User).filter(User.user_id == user_id).first()
        elif email:
            user = db.session.query(User).filter(User.email == email).first()
        elif username:
            user = db.session.query(User).filter(User.username == username).first()
        else:
            return False
    except Exception as e:
        raise DatabaseQueryError("Error Finding User")

    if not user:
        return False

    return True


def is_password_valid(password):
    if not password or not isinstance(password, str):
        return False
    return len(password) >= MIN_PASSWORD


def validate_login_credentials(email, password):
    email = clean_email(email)

    user = db.session.query(User).filter(User.email == email).first()
    if not user:
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
