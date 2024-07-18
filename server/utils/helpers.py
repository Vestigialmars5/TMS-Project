from flask import g

# Compares user's role with a set role, returns true or false TODO: test
def check_user_role(user_id, role):
    try:
        # Get user information TODO: check if this actually gets from g, test if no user
        user = g.user

        # User_id not found
        if not g.user:
            raise ValueError("User not found")

        # Role matches
        if user["role"] == role:
            return True

        # Role doesn't match
        return False

    except Exception as e:
        return str(e)  # TODO: Handle errors (consider what it returns)