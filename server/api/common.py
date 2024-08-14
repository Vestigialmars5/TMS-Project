from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.services import common_service

common_blueprint = Blueprint("common", __name__, url_prefix="/api/common")


@common_blueprint.route("/roles", methods=["GET"])
@jwt_required()
def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """
    if request.method == "GET":

        response = common_service.get_roles()

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500
