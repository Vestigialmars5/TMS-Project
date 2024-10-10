from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from flask import current_app

JWT_ACCESS_EXPIRES = current_app.config.get("JWT_ACCESS_TOKEN_EXPIRES")
JWT_REFRESH_EXPIRES = current_app.config.get("JWT_REFRESH_TOKEN_EXPIRES")


def create_tokens(identity, additional_claims):
    access_token = create_access_token(identity=identity, additional_claims=additional_claims, expires_delta=JWT_ACCESS_EXPIRES)
    refresh_token = create_refresh_token(identity=identity, expires_delta=JWT_REFRESH_EXPIRES)
    return access_token, refresh_token


def decode_jwt(token):
    """
    Decode a JWT token to retrieve its claims.

    :param token (str): The JWT token to decode.
    :return (dict): The decoded claims.
    """
    try:
        decoded_token = decode_token(token)
        return decoded_token
    except Exception as e:
        return None
