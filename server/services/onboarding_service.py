from server.db import get_db
from werkzeug.security import generate_password_hash
from server.utils.token import create_tokens
from flask import abort


class OnboardingService:
    @staticmethod
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

        try:
            db = get_db()
            db.execute(
                "UPDATE users SET email = ?, password = ? WHERE user_id = ?",
                (email, generate_password_hash(password), user_id),
            )

            db.execute(
                "INSERT INTO user_details (user_id, first_name, last_name, phone_number, address) VALUES (?, ?, ?, ?, ?)",
                (user_id, first_name, last_name, phone_number, address),
            )

            db.commit()

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

            return {"success": True, "access_token": access_token}, 200
        except Exception as e:
            abort(400, description=str(e))
