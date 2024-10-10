from server.extensions import db
from server.models.tms_models import User, Role
from werkzeug.security import generate_password_hash
from server.utils.exceptions import DatabaseQueryError
import logging
from server.utils.logging import create_audit_log
from sqlalchemy.exc import IntegrityError
from server.utils.validations import user_exists, validate_delete_user, validate_update_user


logger = logging.getLogger(__name__)


def get_users(search, sort_by, sort_order, page, limit, initiator_id):

    logger.info("Get Users Attempt: by %s", initiator_id)

    try:
        try:
            users = construct_query_users(search, sort_by, sort_order, page, limit)

            logger.info("Get Users Attempt Successful: by %s", initiator_id)
            create_audit_log("Get Users", initiator_id, details="Success")
            return {"success": True, "users": users}

        except Exception as e:
            raise DatabaseQueryError("Error Fetching Users")

    except DatabaseQueryError as e:
        logger.error("Get Users Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Users", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Get Users Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Users", user_id=initiator_id, details="Internal Server Error")
        raise


def create_user(email, password, role_id, initiator_id):
    logger.info("Create User Attempt: by %s", initiator_id)

    try:
        if user_exists(email=email):
            logger.error("Create User Attempt Failed: by %s | User Already Exists", initiator_id)
            create_audit_log("Create User", user_id=initiator_id, details="User Already Exists")
            return {"success": False, "error": "Unique Constraint Violation", "description": "User Already Exists"}
        
        try:
            user = insert_user(email, password, role_id)
        except IntegrityError as e:
            raise DatabaseQueryError("Email Already Exists")
        except Exception as e:
            raise DatabaseQueryError("Error Creating User")


        logger.info("Create User Attempt Successful: by %s | created %s", initiator_id, user.user_id)
        create_audit_log("Create User", user_id=initiator_id, details=f"Created {user.user_id}")
        return {"success": True}

    except DatabaseQueryError as e:
        logger.error("Create User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Create User", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Create User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Create User", user_id=initiator_id, details=e.message)
        raise


def delete_user(user_id, initiator_id):
    logger.info("Delete User Attempt: by %s", initiator_id)

    try:
        is_valid, error = validate_delete_user(user_id, initiator_id)
        if not is_valid:
            if error == "Cannot Delete Self":
                logger.error(
                    "Delete User Attempt Failed: by %s | Cannot Delete Self", initiator_id)
                create_audit_log("Delete User", user_id=initiator_id, details="Cannot Delete Self")
                return {"success": False, "error": "Forbidden", "description": "Cannot Delete Self"}

            else:
                logger.error("Delete User Attempt Failed: by %s | User Does Not Exist", initiator_id)
                create_audit_log("Delete User", user_id=initiator_id, details="User Does Not Exist")
                return {"success": False, "error": "User Not Found", "description": "User Does Not Exist"}

        try:
            db.session.query(User).filter(User.user_id == user_id).delete()
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Deleting User")

        logger.info("Delete User Attempt Successful: by %s | deleted %s", initiator_id, user_id)
        create_audit_log("Delete User", user_id=initiator_id, details=f"Deleted {user_id}")
        return {"success": True}

    except DatabaseQueryError as e:
        logger.error("Delete User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Delete User", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Delete User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Delete User", user_id=initiator_id, details="Internal Server Error")
        raise


def update_user(user_id, email, role_id, initiator_id):
    logger.info("Update User Attempt: by %s", initiator_id)

    try:
        is_valid, user = validate_update_user(user_id, email, role_id, initiator_id)
        if not is_valid:
            if user == "User Does Not Exist":
                logger.error("Update User Attempt Failed: by %s | User Does Not Exist", initiator_id)
                create_audit_log("Update User", user_id=initiator_id, details="User Does Not Exist")
                return {"success": False, "error": "User Not Found", "description": "User Does Not Exist"}
            elif user == "Cannot Update Self":
                logger.error("Update User Attempt Failed: by %s | Cannot Update Self", initiator_id)
                create_audit_log("Update User", user_id=initiator_id, details="Cannot Update Self")
                return {"success": False, "error": "Forbidden", "description": "Cannot Update Self"}
            else:
                logger.info("Update User Attempt Cancelled: by %s | No Changes Made", initiator_id)
                create_audit_log("Update User", user_id=initiator_id, details="No Changes Made")
                return {"success": True, "description": "No Changes Made"}
        
    
        try:
            user.email = email
            user.role_id = role_id
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Updating User")

        logger.info("Update User Attempt Successful: by %s | updated %s", initiator_id, user_id)
        create_audit_log("Update User", user_id=initiator_id, details=f"Updated {user_id}")
        return {"success": True}

    except DatabaseQueryError as e:
        logger.error("Update User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Update User", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Update User Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Update User", user_id=initiator_id, details="Internal Server Error")
        raise


def insert_user(email, password, role_id):
    password_hash = generate_password_hash(password)
    user = User(email=email, password=password_hash, role_id=role_id, status="not_onboarded")
    db.session.add(user)
    db.session.commit()
    return user


def construct_query_users(search, sort_by, sort_order, page, limit):
    """
    Construct the query for getting users.

    @param search (str): The search query.
    @param sort (str): The sort order.
    @param page (int): The page number.
    @param limit (int): The number of items per page.
    @return (str, list): The query and params.
    """

    query = db.session.query(User).join(Role)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (User.email.like(search_filter)) |
            (Role.role_name.like(search_filter))
        )

    if sort_by and sort_order:
        if sort_order == "asc":
            query.order_by(db.asc(sort_by))
        else:
            query.order_by(db.desc(sort_by))

    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)

    users = query.all()

    user_list = [user.to_dict_js() for user in users]

    return user_list


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
