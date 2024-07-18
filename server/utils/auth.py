from flask import jsonify
from functools import wraps

from flask_jwt_extended import get_jwt_identity, jwt_required


# Decorator for roles required
def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                jwt_required()
                current_user_role = get_jwt_identity().get("role")
                if current_user_role not in roles:
                    return jsonify({"error": "Unauthorized access"}), 403
                return f(*args, **kwargs)
            except:
                return jsonify({"error": "Missing or invalid JWT"}), 401

        return decorated_function

    return decorator
