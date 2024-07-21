import sqlite3
from server.db import get_db
from werkzeug.security import generate_password_hash


class ProfileService:
    @staticmethod
    def get_profile(user_id):
        """
        Get the user profile.

        @param user_id (int): The id of the user.
        @return (dict, int): The response and status code.
        """
        try:
            db = get_db()
            res_user = db.execute(
                "SELECT * FROM users WHERE user_id = ?",
                (user_id,),
            )
            user_row = res_user.fetchone()

            res_details = db.execute(
                "SELECT * FROM user_details WHERE user_id = ?",
                (user_id,),
            )
            details_row = res_details.fetchone()

            if user_row and details_row:
                return {
                    "success": True,
                    "profile": {
                        "userId": user_row["user_id"],
                        "username": user_row["username"],
                        "email": user_row["email"],
                        "roleId": user_row["role_id"],
                        "roleName": user_row["role_name"],
                        "firstName": details_row["first_name"],
                        "lastName": details_row["last_name"],
                        "phoneNumber": details_row["phone_number"],
                        "address": details_row["address"],
                    },
                }, 200
            elif not details_row:
                return {"success": False, "error": "User details not found"}, 404
            else:
                return {"success": False, "error": "User not found"}, 404
        except Exception as e:
            print(e)
            return {"success": False, "error": "Error handling db"}, 400

    @staticmethod
    def update_profile(
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

        try:
            db = get_db()
            db.execute(
                "UPDATE users SET email = ?, password = ? WHERE user_id = ?",
                (email, generate_password_hash(password), user_id),
            )

            db.execute(
                "UPDATE user_details SET first_name = ?, last_name = ?, phone_number = ?, address = ? WHERE user_id = ?",
                (first_name, last_name, phone_number, address, user_id),
            )

            db.commit()

            return {"success": True}, 200
        except Exception as e:
            print(e)
            return {"success": False, "error": "Error handling db"}, 400
