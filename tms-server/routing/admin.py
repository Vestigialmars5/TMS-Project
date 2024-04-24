from flask import Blueprint, render_template

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.route("/dashboard")
def dashboard():
    return 
# ADMIN (permision to everything, managing accounts, system config, performance)
# EDIT DATABSE
# ADD USERS
# DELETE ACCOUNTS
# ACCESS TO LOGS


