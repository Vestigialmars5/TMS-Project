import sqlite3 as sql
from flask import g


# Establish db connection, returns db connection from g
def get_db(row=True, db_name="tms_database.db"):
    # Create a connection if doesn't exist
    if "db" not in g:
        g.db = sql.connect(db_name)

        if row:
            # Set queries to return Row objects
            g.db.row_factory = sql.Row
    return g.db


# TODO: Make functions for specific common queries
# Like get contact info, get user credentials info, get role info, etc.