from flask import Blueprint, jsonify
from server.extensions import jwt
from server.utils.exceptions import *
import logging

errors_blueprint = Blueprint("errors", __name__, url_prefix="/api/errors")

logger = logging.getLogger(__name__)


@errors_blueprint.app_errorhandler(400)
def bad_request(error):
    logger.error("Bad Request: %s", error.description)
    response = {
        "success": False,
        "error": "Bad Request",
        "description": error.description,
    }
    return jsonify(response), 400


@errors_blueprint.app_errorhandler(401)
def unauthorized(error):
    logger.error("Unauthorized: %s", error.description)
    response = {
        "success": False,
        "error": "Unauthorized",
        "description": error.description,
    }
    return jsonify(response), 401


@errors_blueprint.app_errorhandler(404)
def not_found(error):
    logger.error("Not Found: %s", error.description)
    response = {
        "success": False,
        "error": "Not Found",
        "description": error.description,
    }
    return jsonify(response), 404


@errors_blueprint.app_errorhandler(500)
def internal_server_error(error):
    logger.error("Internal Server Error: %s", error.description)
    response = {
        "success": False,
        "error": "Internal Server Error",
        "description": error.description,
    }
    return jsonify(response), 500

@errors_blueprint.app_errorhandler(DatabaseError)
def handle_database_error(error):
    logger.error("Database Error: %s", error.message)
    response = {
        "success": False,
        "error": "Database Error",
        "description": error.message,
    }
    return jsonify(response), error.status_code


@errors_blueprint.app_errorhandler(ValidationError)
def handle_validation_error(error):
    logger.error("Validation Error: %s", error.message)
    response = {
        "success": False,
        "error": "Validation Error",
        "description": error.message,
    }
    return jsonify(response), error.status_code


@errors_blueprint.app_errorhandler(Exception)
def handle_exception(error):
    logger.error("Unhandled Exception: %s", error)
    response = {
        "success": False,
        "error": "Unhandled Exception",
        "description": "Internal Server Error",
    }
    return jsonify(response), 500


@jwt.unauthorized_loader
def unauthorized_response(callback):
    logger.error("Unauthorized Access: Missing Authorization Header")
    response = {
        "success": False,
        "error": "Unauthorized Access",
        "description": "Missing Authorization Header",
    }
    return jsonify(response), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    logger.error("Invalid Token: Signature Verification Failed")
    response = {
        "success": False,
        "error": "Invalid Token",
        "description": "Signature verification failed",
    }
    return jsonify(response), 401
