import server.utils.validations as validations
from server.extensions import db
from server.models.tms_models import User, Role
from server.utils.exceptions import DatabaseQueryError


def create_unique_username(username):
    try:
        if validations.user_exists(username=username):
            count = db.session.query(User).filter(
                User.username.like(f"{username}%")).count()
            return f"{username}{count}"
    except Exception as e:
        raise DatabaseQueryError("Error Creating Username")

    return username
