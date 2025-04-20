from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.api.auth import services
from server.utils.data_cleanup import data_cleanup_login

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login user
    Expected data: email, password

    @return (dict, int): The response and status code
    """
    if request.method == "POST":
        # Receive data from request
        try:
            data = request.get_json()
        except:
            abort(400, description="Invalid JSON")

        email, password = data_cleanup_login(data)
    
        response = services.login(email, password)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Invalid Login Credentials":
            return jsonify(response), 401
        elif response["error"] == "Action Not Allowed":
            return jsonify(response), 403
        else:
            return jsonify(response), 500


# TODO: Specify what data is, if it is token make it token
@auth_blueprint.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """
    Logout user.
    Expected data: token.

    @return (dict, int): The response and status code.
    """
    if request.method == "POST":
        # TODO: Check things with token and blacklist etc
        data = request.get_json()
        # Validations -> abort(400, description="Missing Data")
        user_id = get_jwt_identity()

        response = services.logout(user_id)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500


@auth_blueprint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    if request.method == "POST":
        user_id = get_jwt_identity()
        
        response = services.refresh(user_id)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500
        