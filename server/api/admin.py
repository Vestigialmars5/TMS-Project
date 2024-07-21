from flask import Blueprint, jsonify, render_template, request, url_for
from server.db import get_db
from werkzeug.security import generate_password_hash
from server.services.user_service import UserService

admin_blueprint = Blueprint("admin", __name__, url_prefix="/api/admin")


""" 
Oversees the entire system, manages user roles and permissions, and ensures smooth operation of the app.

- **Dashboard**:
  Overview of system performance, key metrics, and notifications.
- **User Management**:
  Add, edit, and remove users. Assign roles and permissions.
- **System Settings**:
  Configure system-wide settings and preferences.
- **Audit Log**:
  View system activity logs for security and compliance.
- **Reports**:
  Generate and view various system reports.
- **Simulation and Testing Environment**:
  Scenario Simulator for testing system resilience and performance.
- **Training and Support Resources**:
  Training Center with video tutorials, user manuals, FAQs, and helpdesk feature.
"""

# User Management
"""
This needs to include the following features:
- Add new users
- Edit user details
- Delete users
- View user details
"""

# TODO: Complete this
@admin_blueprint.route("/users", methods=["POST"])
def create_user():
    """
    Create a user.
    Expected data: (str) email, (str) password, (int) role.

    @return (dict, int): The response and status code.
    """

    if request.method == "POST":

        # TODO: Get data from request
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")
        role_id = data.get("roleId")

        response, status = UserService.create_user(email, password, role_id)

        return jsonify(response), status


@admin_blueprint.route("/users", methods=["GET"])
def get_users():
    """
    Get all users.
    Expected data: (str) search, (str) sort, (int) page, (int) limit.

    @return (dict, int): The response and status code.
    """

    if request.method == "GET":

        search = request.args.get("search", "")
        sort = request.args.get("sort", "asc")
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 25, type=int)

        response, status = UserService.get_users(search, sort, page, limit)

        return jsonify(response), status


@admin_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user.

    @param id (int): The user id.
    @return (dict, int): The response and status code.
    """
    if request.method == "DELETE":

        response, status = UserService.delete_user(user_id)

        return jsonify(response), status


@admin_blueprint.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update a user.
    Expected data: (str) username, (str) email, (int) role.

    @param id (int): The user id.
    @return (dict, int): The response and status code.
    """

    if request.method == "PUT":

        data = request.get_json()

        username = data.get("username")
        email = data.get("email")
        role_id = data.get("roleId")

        response, status = UserService.update_user(user_id, username, email, role_id)

        return jsonify(response), status


# System settings
"""
This needs to include the following features:
- Configure system-wide settings
- Set preferences
- Manage system resources
- Define system roles and permissions

"""


# Audit Log
"""
This needs to include the following features:
- View system activity logs
- Monitor user activity
- Track system events
- Ensure security and compliance

"""


# Reports
"""
This needs to include the following features:
- Generate system reports
- View performance metrics
- Analyze data
- Export reports in various formats
    
"""
