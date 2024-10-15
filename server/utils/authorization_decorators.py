from flask import jsonify, abort
from functools import wraps
from extensions import db
from models.tms_models import User

from flask_jwt_extended import get_jwt_identity
from server.utils.exceptions import DatabaseQueryError
from jwt.exceptions import InvalidTokenError
from sqlalchemy.exc import SQLAlchemyError

# Decorator for roles required


def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                user_id = get_jwt_identity()
                user = db.session.query(User).filter_by(id=user_id).first()
                
            except SQLAlchemyError as e:
                raise DatabaseQueryError("Error Retrieving User Role")
            except Exception:
                raise

            if not user:
                abort(404, description="User Not Found")

            current_user_role = user.role.role_name

            if current_user_role not in roles:
                roles_clean = ", ".join(roles)
                abort(401, description=f"{roles_clean} Required")

            return f(*args, **kwargs)

        return decorated_function

    return decorator
