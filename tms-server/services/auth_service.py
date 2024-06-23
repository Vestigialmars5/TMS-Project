from utils.validation import validate_login_credentials
from utils.token import create_tokens
from db import get_db
import sqlite3
class AuthService:
    @staticmethod
    def login(data):
        """
        Login user with email and password.

        @param data (dict): The data containing email and password.
        @return (dict, int): The response and status code.
        """

        print(data)
        email = data.get("email")
        password = data.get("password")
        role_id = data.get("role_id")

        # TODO: Get rid of these, retrieve from db
        role_name = "Admin"

        user_id = data.get("user_id")

        if validate_login_credentials(email, password):
            access_token = create_tokens(user_id, {"email": email, "roleName": role_name, "roleId": role_id})
            return {"success": True, "access_token": access_token}, 200

        return {"success": False, "error": "Invalid Email Or Password"}, 401

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
            print("Logout successful")
            return {"success": True}, 200
        except Exception as e:
            print("During logout error:", e)
            return {"success": False, "error": str(e)}, 400

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
        except sqlite3.Error as e:
                return {"success": False, "roles": [], "error": "Database error"}, 400
        except Exception as e:
            return {"success": False, "roles": [], "error": e}, 400
