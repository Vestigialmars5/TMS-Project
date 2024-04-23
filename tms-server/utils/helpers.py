from flask import session, g
import sqlite3 as sql
from ..services.user_services import close_db


# Establish db connection, returns db connection from g
def get_db():
    # Create a connection if doesn't exist
    if "db" not in g:
        g.db = sql.connect("tms_database.db")

        # Set queries to return Row objects
        g.db.row_factory = sql.Row
    return g.db


# Compares user's role with a set role, returns true or false TODO: test
def check_user_role(user_id, role):
    try:
        db = get_db()
        res = db.execute("SELECT role FROM users WHERE user_id = ?", (user_id,))
        row = res.fetchone()

        # User_id not found
        if not row:
            raise ValueError("User Id not found")

        # Role matches
        if row["role"] == role:
            return True

        # Role doesn't match
        return False

    except Exception as e:
        return str(e)  # TODO: Handle errors (consider what it returns)

    finally:
        # Close connection regardless of outcome
        close_db()
