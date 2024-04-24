import sqlite3 as sql
from flask import g


# Establish db connection, returns db connection from g
def get_db():
    # Create a connection if doesn't exist
    if "db" not in g:
        g.db = sql.connect("tms_database.db")

        # Set queries to return Row objects
        g.db.row_factory = sql.Row
    return g.db
