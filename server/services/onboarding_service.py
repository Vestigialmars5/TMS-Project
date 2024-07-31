from server.extensions import db
from server.models.tms_models import User, UserDetails
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
            password_hash = generate_password_hash(password)
            # Update user's email and password
            user = db.session.query(User).filter_by(user_id=user_id).first()
            user.email = email
            user.password = password_hash
            db.session.commit()

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
