from flask import Blueprint, jsonify, request, abort
from server.services import user_service
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from server.utils.data_cleanup import data_cleanup_create_user, data_cleanup_get_users, clean_user_id, data_cleanup_update_user
from server.utils.authorization_decorators import roles_required

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


@admin_blueprint.route("/users", methods=["POST"])
@jwt_required()
@roles_required("Admin")
def create_user():
    """
    Create a user.
    Expected data: (str) email, (str) password, (int) role.

    @return (dict, int): The response and status code.
    """

    if request.method == "POST":
        initiator_id = get_jwt_identity()
        # Get data from request
        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        email, password, role_id = data_cleanup_create_user(data)

        response = user_service.create_user(
            email, password, role_id, initiator_id)

        if response["success"]:
            return jsonify(response), 201
        elif response["error"] == "Unique Constraint Violation":
            return jsonify(response), 409
        else:
            return jsonify(response), 500


@admin_blueprint.route("/users", methods=["GET"])
@jwt_required()
@roles_required("Admin")
def get_users():
    if request.method == "GET":

        search, sort_by, sort_order, page, limit = data_cleanup_get_users(
            request.args)

        initiator_id = get_jwt_identity()

        response = user_service.get_users(
            search, sort_by, sort_order, page, limit, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500


@admin_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
@roles_required("Admin")
def delete_user(user_id):
    """
    Delete a user.

    @param id (int): The user id.
    @return (dict, int): The response and status code.
    """
    if request.method == "DELETE":

        initiator_id = get_jwt_identity()

        user_id = clean_user_id(user_id)

        response = user_service.delete_user(user_id, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "User Not Found":
            return jsonify(response), 404
        elif response["error"] == "Forbidden":
            return jsonify(response), 403
        else:
            return jsonify(response), 500


@admin_blueprint.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
@roles_required("Admin")
def update_user(user_id):
    """
    Update a user.
    Expected data: (str) email, (int) role.

    @param id (int): The user id.
    @return (dict, int): The response and status code.
    """

    if request.method == "PUT":

        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        email, role_id = data_cleanup_update_user(data)
        user_id = clean_user_id(user_id)

        initiator_id = get_jwt_identity()

        response = user_service.update_user(
            user_id, email, role_id, initiator_id)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Forbidden":
            return jsonify(response), 403
        elif response["error"] == "User Not Found":
            return jsonify(response), 404
        elif response["error"] == "Unique Constraint Violation":
            return jsonify(response), 409
        else:
            return jsonify(response), 500


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
