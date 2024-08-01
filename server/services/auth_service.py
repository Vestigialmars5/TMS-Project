from server.utils.validation import validate_login_credentials
from server.utils.token import create_tokens
from flask import abort
from server.utils.logging import log_error
from ..extensions import db
from ..models.tms_models import User, UserDetails, Role


class AuthService:
    @staticmethod
    def login(data):
        """
        Login user with email and password.

        @param data (dict): The data containing email and password.
        @return (dict, int): The response and status code.
        """

        email = data.get("email")
        password = data.get("password")
        role_id = data.get("role_id")

        # TODO: Get rid of these, retrieve from db
        # Maybe even from profile_service
        role_name = "Admin"

        user_id = data.get("user_id")

        if validate_login_credentials(email, password):
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
                log_error(e)
                abort(400, description="Error Fetching User Details")

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
            return {"success": True, "access_token": access_token}, 200

        abort(401, description="Email Or Password Is Incorrect")

    # TODO: Finish this
    @staticmethod
    def logout(data):
        """
        Logout user.

        @param data (dict): The data containing the token.
        @return (dict, int): The response and status code.
        """

        try:
            # TODO: Add jti and blacklist for tokens
            return {"success": True}, 200
        except Exception as e:
            log_error(e)
            abort(400, description="Error Handling JWT")

    @staticmethod
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
            
            return {"success": True, "roles": roles}, 200
        except Exception as e:
            log_error(e)
            abort(500, description="Error Fetching Roles")
