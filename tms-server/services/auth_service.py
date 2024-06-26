from utils.validation import validate_login_credentials
from utils.token import create_tokens
from db import get_db
import sqlite3
from flask import abort


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
            db = get_db()
            res = db.execute(
                "SELECT first_name, last_name FROM user_details WHERE user_id = ?",
                (user_id,),
            )
            row = res.fetchone()

            if not row:
                first_name = ""
                last_name = ""
                isOnboarding_completed = False
            else:
                first_name = row["first_name"]
                last_name = row["last_name"]
                isOnboarding_completed = True

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
            abort(400, description=str(e))

    @staticmethod
    def get_roles():
        """
        Get all roles.

        @return (dict, int): The response and status code.
        """
        try:
            db = get_db()
            res = db.execute("SELECT * FROM roles")
            rows = res.fetchall()
            roles = []
            for row in rows:
                roles.append(
                    {
                        "roleId": row["role_id"],
                        "roleName": row["role_name"],
                    }
                )
            return {"success": True, "roles": roles}, 200
        except sqlite3.OperationalError as e:
            return {"success": False, "roles": [], "error": str(e)}, 400
        except Exception as e:
            return {"success": False, "roles": [], "error": str(e)}, 400
