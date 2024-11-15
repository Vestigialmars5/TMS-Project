from server.extensions import db
from server.models.tms_models import User, UserDetails, CustomerDetails
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from server.utils.exceptions import *
from datetime import timedelta
from flask import current_app
from server.utils.logging import create_audit_log
import logging
import traceback

logger = logging.getLogger(__name__)


def onboard_user_details(
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
    logger.info("Onboarding Step 1 Attempt: by %s", user_id)
    try:
        onboarding_step = get_onboarding_step(user_id)

        if onboarding_step == -1 or onboarding_step > 1:
            logger.error(
                "Onboard 1 Attempt Failed: by %s | Wrong Step", user_id)
            create_audit_log("Onboard 1", user_id=user_id,
                             details="Wrong Step")
            return {"success": False, "error": "Wrong Step", "description": "Current Step Is Out Of Sync"}

        if onboarding_step == 0:
            logger.warning(
                "Onboard 1 Attempt Failed: by %s | User Already Onboarded", user_id)
            create_audit_log("Onboard 1", user_id=user_id,
                             details="User Already Onboarded")
            return {"success": False, "error": "Action Was Already Completed", "description": "User Already Onboarded"}

        # Check if password and confirmation match
        if password != confirmation:
            logger.warning(
                "Onboard 1 Attempt Failed: by %s | Passwords Do Not Match", user_id)
            create_audit_log("Onboard 1", user_id=user_id,
                             details="Passwords Do Not Match")
            return {"success": False, "error": "Passwords Do Not Match", "description": "Password and Confirmation Do Not Match"}

        try:
            user = db.session.query(User).filter(
                User.user_id == user_id).first()

            update_user_password(user, password)

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

        user_info = {
            "userId": user_id,
            "status": user.status,
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "roleName": role_name,
            "roleId": role_id,
        }

        logger.info("Onboard 1 Attempt Successful: by %s", user_id)
        create_audit_log("Onboard 1", user_id=user_id, details="Success")
        return {"success": True, "user": user_info}

    except DatabaseQueryError as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Onboard Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard", user_id=user_id,
                         details="Internal Server Error")
        raise


def onboard_customer_details(user_id, role_id, company_name, company_address):
    logger.info("Onboarding Step 2 Attempt: by %s", user_id)

    try:
        onboarding_step = get_onboarding_step(user_id, role_id)
        print(onboarding_step)
        if onboarding_step == -1:
            logger.error(
                "Onboard Step 2 Attempt Failed: by %s | Invalid Role ID", user_id)
            create_audit_log("Onboard 2", user_id=user_id,
                             details="Invalid Role ID")
            raise DataValidationError("Invalid Role ID")

        if onboarding_step == 0:
            logger.warning(
                "Onboard Step 2 Attempt Failed: by %s | User Already Onboarded", user_id)
            create_audit_log("Onboard 2", user_id=user_id,
                             details="User Already Onboarded")
            return {"success": False, "error": "Action Was Already Completed", "description": "User Already Onboarded"}

        if onboarding_step == 1 or onboarding_step > 2:
            logger.warning(
                "Onboard Step 2 Attempt Failed: by %s | Wrong Step", user_id)
            create_audit_log("Onboard 2", user_id=user_id,
                             details="Wrong Step")
            return {"success": False, "error": "Wrong Step", "description": "Onboard Step 1 Not Completed"}

        try:
            customer_details = CustomerDetails(
                user_id=user_id,
                company_name=company_name,
                company_address=company_address
            )
            db.session.add(customer_details)
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Adding Customer Details")

        # Currently, step 2 is final step. Update user status to active
        try:
            user = db.session.query(User).filter_by(user_id=user_id).first()
            user.status = "active"
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Updating User Status")

        role_name = user.role.role_name

        user_info = {
            "userId": user_id,
            "email": user.email,
            "firstName": user.user_details.first_name,
            "lastName": user.user_details.last_name,
            "roleName": role_name,
            "roleId": role_id,
            "customerDetails": {
                "companyName": company_name,
                "companyAddress": company_address
            }
        }

        logger.info("Onboard Step 2 Attempt Successful: by %s", user_id)
        create_audit_log("Onboard 2", user_id=user_id, details="Success")
        return {"success": True, "user": user_info}

    except DatabaseQueryError as e:
        logger.error("Onboard Step 2 Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard 2", user_id=user_id, details=e.message)
        raise

    except DataValidationError as e:
        logger.error("Onboard Step 2 Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard 2", user_id=user_id, details=e.message)
        raise

    except Exception as e:
        print(traceback.format_exc())
        logger.error("Onboard Step 2 Attempt Failed: by %s | %s", user_id, e)
        create_audit_log("Onboard 2", user_id=user_id,
                         details="Internal Server Error")
        raise


def get_customer_details(user_id):
    customer_details = db.session.query(
        CustomerDetails).filter_by(user_id=user_id).first()
    return customer_details


role_details_handler = {
    1: "",  # Admin
    2: "",  # Transportation Manager
    3: "",  # Carrier
    4: get_customer_details,  # Customer/Shipper
    5: "",  # Driver
    6: "",  # Finance/Accounting
    7: "",  # Warehouse Manager
}


def get_onboarding_step(user_id, role_id=None):
    try:
        user_details = db.session.query(
            UserDetails).filter_by(user_id=user_id).first()

        if user_details is None:
            return 1

        if role_id is None:
            user = db.session.query(User).filter_by(user_id=user_id).first()
            if user is None:
                return -1
            role_id = user.role_id

        handler = role_details_handler.get(role_id)
        if handler is None:
            return -1

        role_details = handler(user_id)

        if role_details is None:
            return 2

        return 0

    except Exception as e:
        logger.error("Get Step Attempt Failed: by %s | %s", user_id, e)
        return -1


def update_user_password(user, password):
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
