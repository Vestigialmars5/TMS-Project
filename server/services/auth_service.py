from server.utils.validations import validate_login_credentials
from server.utils.token import create_tokens
from server.utils.logging import create_audit_log
from ..extensions import db
from ..models.tms_models import User, UserDetails, Role
from server.utils.exceptions import DatabaseQueryError
import logging

logger = logging.getLogger(__name__)


def login(email, password):
    """
    Login user with email and password.

    @param data (dict): The data containing email and password.
    @return (dict, int): The response and status code.
    """
    logger.info("Login Attempt: by %s", email)

    try:
        # Check if email and password are valid
        if not validate_login_credentials(email, password):
            logger.warning("Login Attempt Failed: by %s | Invalid Credentials", email)
            create_audit_log("Login", email=email, details="Invalid Credentials")
            return {"success": False, "error": "Invalid Credentials", "description": "Email Or Password Incorrect"}

        # Retrieve user details, if not found onboarding is not completed
        try:
            user = db.session.query(User).filter(User.email == email).first()
            first_name, last_name = get_first_name_last_name(user.user_id)
        except Exception as e:
            raise DatabaseQueryError("Error Retrieving User Data")

        if first_name and last_name:
            is_onboarding_completed = True
        else:
            is_onboarding_completed = False

        access_token = create_tokens(
            user.user_id,
            {
                "isOnboardingCompleted": is_onboarding_completed,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "roleName": user.role.role_name,
                "roleId": user.role_id,
            },
        )

        logger.info("Login Attempt Successful: by %s", user.user_id)
        create_audit_log("Login", user_id=user.user_id, details="Success")
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
    logger.info("Logout Attempt: by %s", "Placeholder")

    try:
        # TODO: Add jti and blacklist for tokens
        return {"success": True}
    except Exception as e:
        # TODO: User info
        logger.error("Logout Attempt Failed: by %s", e)
        create_audit_log("Logout", user_id=data.get("user_id"), details="Internal Server Error")
        raise


def get_first_name_last_name(user_id):
    query = db.select(UserDetails.first_name, UserDetails.last_name).filter(
        UserDetails.user_id == user_id)
    res = db.session.execute(query).first()
    if not res:
        return None, None
    return res.first_name, res.last_name
