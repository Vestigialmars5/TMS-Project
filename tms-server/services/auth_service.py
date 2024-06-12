from utils.validation import validate_login_credentials
from utils.token import create_tokens


class AuthService():
    @staticmethod
    def login(data):
        email = data.get(email)
        password = data.get(password)

        # TODO: Get rid of these
        role = data.get(role)
        user_id = data.get(user_id)


        if not validate_login_credentials(email, password):
            access_token = create_tokens(user_id, {email, role})
            return {"success": True, "access_token": access_token}, 200
            
        return {"success": False, "error": "Invalid Email Or Password"}, 401