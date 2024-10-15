from server.extensions import db
from server.models.tms_models import User, UserDetails
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from server.utils.exceptions import *
from datetime import timedelta
from flask import current_app
from server.utils.logging import create_audit_log
import logging

logger = logging.getLogger(__name__)


def onboard_user(
    user_id,
    email,
    password,
    confirmation,
    first_name,
    last_name,
    phone_number,
    address,
):

    # TODO: Validation
    logger.info("Onboard Attempt: by %s", user_id)
    try:
        # Check if user already onboarded
        if not is_onboarded(user_id):
            logger.warning(
                "Onboard Attempt Failed: by %s | User Already Onboarded", user_id)
            create_audit_log("Onboard", user_id=user_id,
                             details="User Already Onboarded")
            return {"success": False, "error": "Action Was Already Completed", "description": "User Already Onboarded"}

        # Check if password and confirmation match
        if password != confirmation:
            logger.warning(
                "Onboard Attempt Failed: by %s | Passwords Do Not Match", user_id)
            create_audit_log("Onboard", user_id=user_id,
                             details="Passwords Do Not Match")
            return {"success": False, "error": "Passwords Do Not Match", "description": "Password and Confirmation Do Not Match"}

        try:
            status = "active"
            user = db.session.query(User).filter(
                User.user_id == user_id).first()

            if user is None:
                raise DatabaseQueryError("User Not Found")

            update_user(user, password, status)
        except DatabaseQueryError as e:
            raise
        except Exception as e:
            raise DatabaseQueryError("Error Updating Password")

        try:
            # Insert other details into user_details table
            update_user_details(user_id, first_name,
                                last_name, phone_number, address)
        except Exception as e:
            raise DatabaseQueryError("Error Adding User Details")

        role_id = user.role_id
        role_name = user.role.role_name

        access_exp_hours = current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] / 3600

        access_token = create_access_token(
            user_id, expires_delta=timedelta(hours=access_exp_hours)
        )

        user_info = {
            "userId": user_id,
            "status": status,
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "roleName": role_name,
            "roleId": role_id,
        }

        logger.info("Onboard Attempt Successful: by %s", user_id)
        create_audit_log("Onboard", user_id=user_id, details="Success")
        return {"success": True, "accessToken": access_token, "user": user_info}

    except DatabaseQueryError as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id,
                         details="Internal Server Error")
        raise


def is_onboarded(user_id):
    user_details = db.session.query(
        UserDetails).filter_by(user_id=user_id).first()

    if user_details is not None:
        return False
    else:
        return True


def update_user(user, password, status):
    user.password = generate_password_hash(password)
    user.status = status
    db.session.commit()


def update_user_details(user_id, first_name, last_name, phone_number, address):
    user_details = UserDetails(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
    )
    db.session.add(user_details)
    db.session.commit()
