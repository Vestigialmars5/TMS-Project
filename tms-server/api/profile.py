from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from jwt_config import jwt
from services.profile_service import ProfileService

profile_blueprint = Blueprint("profile", __name__, url_prefix="/api/onboarding")


@profile_blueprint.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    """
    Get the user profile.

    @return (dict, int): The response and status code.
    """

    user_id = jwt.get_jwt_identity()

    response, status = ProfileService.get_profile(user_id)

    return jsonify(response), status