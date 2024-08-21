from server.extensions import db
from server.models.tms_models import User, Role
from werkzeug.security import generate_password_hash
from server.utils.exceptions import DatabaseQueryError
import logging
from server.utils.logging import create_audit_log
from sqlalchemy.exc import IntegrityError
from server.utils.validations import user_exists
from server.utils.helpers import create_unique_username


logger = logging.getLogger(__name__)


def get_users(search, sort_by, sort_order, page, limit, initiator_id):
    """
    Get all users.

    @param search (str): The search query.
    @param sortBy (str): The sort by field.
    @param sortOrder (str): The sort order.
    @param page (int): The page number.
    @param limit (int): The number of items per page.
    @return (dict, int): The response and status code.
    """
    logger.info("Get Users Attempt: by %s", initiator_id)
    try:
        try:
            users = _construct_query(
                search, sort_by, sort_order, page, limit)

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
    """
    Create a user.

    @param email (str): The email of the user.
    @param password (str): The password of the user.
    @param role_id (int): The role_id of the user.
    @return (dict, int): The response and status code.
    """
    logger.info("Create User Attempt: by %s", initiator_id)

    try:

        try:
            if not user_exists(email=email):
                logger.error("Create User Attempt Failed: by %s | User Already Exists", initiator_id)
                create_audit_log("Create User", user_id=initiator_id, details="User Already Exists")
                return {"success": False, "error": "Unique Constraint Violation", "description": "User Already Exists"}
        except:
            raise DatabaseQueryError("Error Checking User")

        try:
            simple_username = email.split("@")[0]
            username = create_unique_username(simple_username)
        except Exception as e:
            raise DatabaseQueryError("Error Creating Username")


        try:
            user = insert_user(email, username, password, role_id)
        except IntegrityError as e:
            raise DatabaseQueryError("Username Already Exists")
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
    """
    Delete a user.

    @param user_id (int): The id of the user.
    @return (dict, int): The response and status code.
    """
    # TODO: Validations for deleting
    logger.info("Delete User Attempt: by %s", initiator_id)

    try:
        try:
            db.session.query(User).filter(User.user_id == user_id).delete()
            db.session.commit()
        except Exception as e:
            raise DatabaseQueryError("Error Deleting User")

        logger.info(
            "Delete User Attempt Successful: by %s | deleted %s", initiator_id, user_id)
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


def update_user(user_id, username, email, role_id, initiator_id):
    """
    Update a user.

    @param user_id (int): The id of the user.
    @param username (str): The username of the user.
    @param email (str): The email of the user.
    @param role_id (int): The role_id of the user.
    @return (dict, int): The response and status code.
    """
    logger.info("Update User Attempt: by %s", initiator_id)

    try:
        # TODO: Validations for updating
        try:
            user = db.session.query(User).filter(User.user_id == user_id).first()
            user.username = username
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


def _construct_query(search, sort_by, sort_order, page, limit):
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
            (User.username.like(search_filter)) |
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


def insert_user(email, username, password, role_id):
    password_hash = generate_password_hash(password)
    user = User(username=username, email=email,
                password=password_hash, role_id=role_id)
    db.session.add(user)
    db.session.commit()
    return user