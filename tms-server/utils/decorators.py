from flask import redirect, session
from functools import wraps


# Define login_required decorator, redirects to login if not logged in
""" Change per user """
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id"):
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    return decorated_function
