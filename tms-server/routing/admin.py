from flask import Blueprint, render_template, url_for

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.route("/")
def index():
    return "<p>Hello, World!</p>"

# ADMIN (permision to everything, managing accounts, system config, performance)
# EDIT DATABSE
# ADD USERS
# DELETE ACCOUNTS
# ACCESS TO LOGS
