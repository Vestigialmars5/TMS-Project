from server.utils.validations import validate_login_credentials
from flask import current_app
from server.utils.logging import create_audit_log
from ...extensions import db
from ...models.tms_models import User, UserDetails, Role
from server.utils.exceptions import DatabaseQueryError
import logging
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


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

        try:
            user = db.session.query(User).filter(User.email == email).first()
            if user.status == "not_onboarded":
                first_name, last_name = "", ""
            
            # Until I figure out how to handle this
            #elif user.status == "active":
                #return {"success": False, "error": "Action Not Allowed", "description": "User Already Logged In"}
            
            else:
                first_name, last_name = get_first_name_last_name(user.user_id)
                user.status = "active"
                db.session.commit()

        except Exception as e:
            raise DatabaseQueryError("Error Retrieving User Data")

        # TODO: Add to_dict_js maybe, depends if i want the created and updated at
        access_exp_hours = current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] / 3600
        refresh_exp_days = current_app.config['JWT_REFRESH_TOKEN_EXPIRES'] / 86400
        
        access_token = create_access_token(
            user.user_id, expires_delta=timedelta(hours=access_exp_hours)
        )

        refresh_token = create_refresh_token(
            user.user_id, expires_delta=timedelta(days=refresh_exp_days)
        )

        user_info = {
            "userId": user.user_id,
            "email": email,
            "status": user.status,
            "firstName": first_name,
            "lastName": last_name,
            "roleName": user.role.role_name,
            "roleId": user.role_id,
        }

        logger.info("Login Attempt Successful: by %s", user.user_id)
        create_audit_log("Login", user_id=user.user_id, details="Success")
        return {"success": True, "accessToken": access_token, "refreshToken": refresh_token, "user": user_info}

    except DatabaseQueryError as e:
        logger.error("Login Attempt Failed: by %s | %s", email, e)
        create_audit_log("Login", email=email, details=e.message)
        raise

    except Exception as e:
        logger.error("Login Attempt Failed: by %s | %s", email, e)
        create_audit_log("Login", email=email,
                         details="Internal Server Error")
        raise


def logout(user_id):
    """
    Logout user.

    @param data (dict): The data containing the token.
    @return (dict, int): The response and status code.
    """
    logger.info("Logout Attempt: by %s", "Placeholder")

    try:
        # TODO: Add jti and blacklist for tokens

        try:
            user = db.session.query(User).filter(
                User.user_id == user_id).first()
            user.status = "inactive"
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Updating User Status")

        logger.info("Logout Attempt Successful: by %s", user_id)
        create_audit_log("Logout", user_id=user_id, details="Success")
        return {"success": True}

    except Exception as e:
        # TODO: User info
        logger.error("Logout Attempt Failed: by %s", e)
        create_audit_log("Logout", user_id=user_id,
                         details="Internal Server Error")
        raise


def get_first_name_last_name(user_id):
    query = db.select(UserDetails.first_name, UserDetails.last_name).filter(
        UserDetails.user_id == user_id)
    res = db.session.execute(query).first()
    if not res:
        return "", ""
    return res.first_name, res.last_name
