from server.extensions import db
from server.models.tms_models import User, UserDetails
from werkzeug.security import generate_password_hash
from server.utils.token import create_tokens
from server.utils.exceptions import *
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
    role_id,
    role_name,
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
            update_password(user_id, password)
        except Exception as e:
            raise DatabaseQueryError("Error Updating Password")

        try:
            # Insert other details into user_details table
            update_user_details(user_id, first_name,
                                last_name, phone_number, address)
        except Exception as e:
            raise DatabaseQueryError("Error Adding User Details")

        access_token = create_tokens(
            user_id,
            {
                "isOnboardingCompleted": True,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "roleName": role_name,
                "roleId": role_id,
            },
        )

        logger.info("Onboard Attempt Successful: by %s", user_id)
        create_audit_log("Onboard", user_id=user_id, details="Success")
        return {"success": True, "accessToken": access_token}

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


def update_password(user_id, password):
    user = db.session.query(User).filter(User.user_id == user_id).first()
    user.password = generate_password_hash(password)
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
