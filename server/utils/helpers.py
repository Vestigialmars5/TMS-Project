from server.models.tms_models import User
from server.extensions import db

def get_user_role_id(user_id):
    user = db.session.query(User).filter_by(user_id=user_id).first()
    role_id = user.role_id
    return role_id