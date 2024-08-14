from server.extensions import db
from server.models.tms_models import Role
from server.utils.exceptions import DatabaseQueryError
import logging

logger = logging.getLogger(__name__)

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
