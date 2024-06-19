from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from datetime import timedelta

# TODO: Implement token expiry Configuration for token expiry
# ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)


def create_tokens(identity, additional_claims):
    """
    Create JWT access token.

    :param identity (int): The user id.
    :param additional_claims (dict): Data that will be passed for easy access to the client, like email and role.
    :return (str): Access token.
    """
    access_token = create_access_token(
        identity=identity, additional_claims=additional_claims
    )
    # TODO: Implement refresh token

    return access_token


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
