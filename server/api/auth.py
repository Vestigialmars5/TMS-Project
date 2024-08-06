from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required
from server.services.auth_service import AuthService
from ..extensions import db
import logging
import traceback
from ..models.tms_models import User, AuditLog
from ..services.exceptions import InvalidCredentials, DatabaseQueryError
from server.utils.logging import create_audit_log

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

# TODO: check auth libraries
# TODO: Add role based access control

logger = logging.getLogger(__name__)

# TODO: Complete login
@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login user
    Expected data: email, password

    @return (dict, int): The response and status code
    """
    if request.method == "POST":
        # Receive data from request
        data = request.get_json()

        # TODO: Get rid of this, for testing admin
        """res = db.execute("SELECT * FROM users WHERE user_id = ?", (1,))
        row = res.fetchone()
        user_id = row["user_id"]
        email = row["email"]
        password = row["password"]
        role = row["role_id"] """


        try:
            user = db.session.query(User).filter(User.user_id == 1).first()
        except Exception as e:
            abort(500, description="Error Retrieving Data")

        temp_data = {
            "email": user.email,
            "password": user.password,
            "role_id": user.role_id,
            "user_id": user.user_id,
        }

        logger.info(f"Login Attempt: {temp_data['email']}")

        # TODO: Pass actual data
        try:
            response, status = AuthService.login(temp_data)
            logger.info(f"Login Successful: {temp_data['email']}")
            create_audit_log(temp_data["user_id"], "Login", "Login Attempt Successful")
            return jsonify(response), status
        except InvalidCredentials as e:
            logger.warning(f"Login Attempt Failed: {temp_data['email']} - Invalid Credentials")
            create_audit_log(temp_data["user_id"], "Login", "Login Attempt Failed: Invalid Credentials")
            abort(401, description="Email Or Password Is Incorrect")
        except DatabaseQueryError as e:
            logger.error(f"Login Attempt Failed: {temp_data['email']} - {traceback.format_exc()}")
            create_audit_log(temp_data["user_id"], "Login", "Login Attempt Failed: Database Query Error")
            abort(500, description="Error Retrieving Data")
        except Exception as e:
            logger.error(f"Login Attempt Failed: {temp_data['email']} - {traceback.format_exc()}")
            create_audit_log(temp_data["user_id"], "Login", "Login Attempt Failed: Unexpected Error")
            abort(500, description="Unexpected Error")


# TODO: Specify what data is, if it is token make it token
@auth_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    Logout user.
    Expected data: token.

    @return (dict, int): The response and status code.
    """
    if request.method == "POST":
        data = request.get_json()
        response, status = AuthService.logout(data)

        return jsonify(response), status


@auth_blueprint.route("/roles", methods=["GET"])
@jwt_required()
def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """
    if request.method == "GET":
        response, status = AuthService.get_roles()

        return jsonify(response), status
