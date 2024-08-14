# Use validator class to validate data
from server.utils.validator import *
from server.extensions import db
from server.models.tms_models import *
from werkzeug.security import check_password_hash
from server.utils.exceptions import DatabaseQueryError, InvalidDataError

# TODO: Get roles from db

# TODO: Complete this
def validate_login_credentials(email, password):
    email = clean_email(email)

    user = db.session.query(User).filter(User.email == email).first()
    if not user:
        return False
    
    # TODO: Uncomment -Ignores if password is wrong
    """ if not check_password_hash(user.password, password):
        return False """

    return True

def get_first_name_last_name(user_id):
    query = db.select(UserDetails.first_name, UserDetails.last_name).filter(
        UserDetails.user_id == user_id)
    res = db.session.execute(query).first()
    if not res:
        return None, None
    return res.first_name, res.last_name


# TODO: Validations for registering
def validate_register_credentials(email, username, password, role):
    # TODO: Validations between data being passed and from db
    return True
