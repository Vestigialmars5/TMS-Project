from server.utils.validation import validate_login_credentials
from server.utils.token import create_tokens
from flask import abort
from server.utils.logging import create_audit_log
from ..extensions import db
from ..models.tms_models import User, UserDetails, Role
from server.services.exceptions import DatabaseQueryError
import logging

logger = logging.getLogger(__name__)


def login(data):
    """
    Login user with email and password.

    @param data (dict): The data containing email and password.
    @return (dict, int): The response and status code.
    """
    email = data.get("email")
    password = data.get("password")
    role_id = data.get("role_id")

    logger.info("Login Attempt: by %s", data.get("email"))

    try:

        # TODO: Get rid of these, retrieve from db
        # Maybe even from profile_service
        role_name = "Admin"

        user_id = data.get("user_id")

        if not validate_login_credentials(email, password):
            logger.warning(
                "Login Attempt Failed: by %s | Invalid Credentials", email)
            create_audit_log("Login", email=email,
                             details="Invalid Credentials")
            return {"success": False, "error": "Invalid Credentials", "description": "Email Or Password Incorrect"}

        try:
            query = db.select(UserDetails.first_name, UserDetails.last_name).filter(
                UserDetails.user_id == user_id)
            res = db.session.execute(query).first()

            if res is not None:
                first_name, last_name = res
                isOnboarding_completed = True
            else:
                first_name, last_name = "", ""
                isOnboarding_completed = False
        except Exception as e:
            raise DatabaseQueryError("Error Retrieving Data")

        access_token = create_tokens(
            user_id,
            {
                "isOnboardingCompleted": isOnboarding_completed,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "roleName": role_name,
                "roleId": role_id,
            },
        )

        logger.info("Login Attempt Successful: by %s", user_id)
        create_audit_log("Login", user_id=user_id, details="Success")
        return {"success": True, "access_token": access_token}

    except DatabaseQueryError as e:
        logger.error("Login Attempt Failed: by %s | %s", email, e)
        create_audit_log("Login", email=email, details=e.message)
        raise

    except Exception as e:
        logger.error("Login Attempt Failed: by %s | %s", email, e)
        create_audit_log("Login", email=email,
                         details="Internal Server Error")
        raise


def logout(data):
    """
    Logout user.

    @param data (dict): The data containing the token.
    @return (dict, int): The response and status code.
    """

    try:
        # TODO: Add jti and blacklist for tokens
        return {"success": True}
    except Exception as e:
        # TODO: User info
        logger.error("Logout Attempt Failed: by %s", e)
        create_audit_log("Logout", user_id=data.get("user_id"), details="Internal Server Error")
        raise


def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """

    try:
        # Get all roles from db
        roles_res = db.session.query(Role).all()
        roles = []
        for role in roles_res:
            roles.append(
                {
                    "roleId": role.role_id,
                    "roleName": role.role_name
                }
            )

        return {"success": True, "roles": roles}
    except Exception as e:
        logger.error("Error Fetching Roles: %s", e)
        raise DatabaseQueryError("Error Fetching Roles")
