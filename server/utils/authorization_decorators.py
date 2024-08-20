from flask import jsonify, abort
from functools import wraps

from flask_jwt_extended import get_jwt
from jwt.exceptions import InvalidTokenError

# Decorator for roles required


def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                current_user_role = get_jwt()["roleName"]
            except Exception as e:
                raise e

            if current_user_role not in roles:
                abort(401, description=f"{roles} Required")

            return f(*args, **kwargs)

        return decorated_function

    return decorator
