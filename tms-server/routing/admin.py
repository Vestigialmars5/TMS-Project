from flask import session, g
import sqlite3 as sql

# Close db connection after every request
@app.teardown_appcontext
def close_db(exception):
    if "db" in g:
        g.db.close()


# ADMIN (permision to everything, managing accounts, system config, performance)
# EDIT DATABSE
# ADD USERS
# DELETE ACCOUNTS
# ACCESS TO LOGS


