import server.utils.validations as validations
from server.extensions import db
from server.models.tms_models import User


def create_unique_username(username):

    if validations.user_exists(username=username):
        count = db.session.query(User).filter(
            User.username.like(f"{username}%")).count()
        return f"{username}{count}"

    return username
