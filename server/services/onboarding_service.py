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
        if not isOnboarded(user_id):
            return {"success": False, "error": "User Already Onboarded"}

        try:
            password_hash = generate_password_hash(password)
            # Update user's email and password
            user = db.session.query(User).filter_by(user_id=user_id).first()
            user.email = email
            user.password = password_hash
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Updating User")

        try:
            # Insert other details into user_details table
            user_detail = UserDetails(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                address=address,
            )
            db.session.add(user_detail)
            db.session.commit()
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
        return {"success": True, "access_token": access_token}

    except DatabaseQueryError as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id, details="Internal Server Error")
        raise


def isOnboarded(user_id):
    user_details = db.session.query(UserDetails).filter_by(user_id=user_id).first()

    if user_details is not None:
        return False
    else:
        return True