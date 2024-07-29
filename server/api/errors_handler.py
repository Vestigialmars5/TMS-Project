from flask import Blueprint, jsonify
from server.extensions import jwt
from werkzeug.exceptions import HTTPException
import json


errors_blueprint = Blueprint("errors", __name__, url_prefix="/api/errors")


@errors_blueprint.app_errorhandler(400)
def bad_request(error):
    print(error.description)
    response = {
        "success": False,
        "error": "Bad Request",
        "description": error.description,
    }
    return jsonify(response), 400


@errors_blueprint.app_errorhandler(401)
def unauthorized(error):
    print(error.description)

    response = {
        "success": False,
        "error": "Unauthorized",
        "description": error.description,
    }
    return jsonify(response), 401


@errors_blueprint.app_errorhandler(404)
def not_found(error):
    print(error.description)

    response = {
        "success": False,
        "error": "Not Found",
        "description": error.description,
    }
    return jsonify(response), 404


@errors_blueprint.app_errorhandler(500)
def internal_server_error(error):
    print(error.description)

    response = {
        "success": False,
        "error": "Internal Server Error",
        "description": error.description,
    }
    return jsonify(response), 500


@errors_blueprint.app_errorhandler(HTTPException)
def handle_exception(error):
    response = error.get_response()
    response.data = json.dumps(
        {
            "success": False,
            "error": error.name,
            "description": error.description,
        }
    )
    response.content_type = "application/json"
    return response


@jwt.unauthorized_loader
def unauthorized_response(callback):
    response = {
        "success": False,
        "error": "Unauthorized Access",
        "description": "Missing Authorization Header",
    }
    return jsonify(response), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    response = {
        "success": False,
        "error": "Invalid Token",
        "description": "Signature verification failed",
    }
    return jsonify(response), 401
