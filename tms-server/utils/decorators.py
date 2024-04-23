from flask import redirect, session
from functools import wraps


# Define login_required decorator, redirects to login if not logged in
def login_required(role_required):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get("user_id"):
                # Check if user's role matches role required
                if check_user_role(session.get("user_id"), role_required): # TODO: Make this function
                    return f(*args, **kwargs)
                else:
                    # TODO: Make this redirect
                    return redirect("/unauthorized")
            else:
                # TODO: Make this redirect
                return redirect("/login")
        return decorated_function
    return decorator
