from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required
from server.services import auth_service
from ..extensions import db
from ..models.tms_models import User

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")

# TODO: check auth libraries
# TODO: Add role based access control

# TODO: Complete login


@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login user
    Expected data: email, password

    @return (dict, int): The response and status code
    """
    if request.method == "POST":
        # Receive data from request
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        # Validations -> abort(400, description="Missing Data")

        # TODO: Get rid of this, for testing admin
        """res = db.execute("SELECT * FROM users WHERE user_id = ?", (1,))
        row = res.fetchone()
        user_id = row["user_id"]
        email = row["email"]
        password = row["password"]
        role = row["role_id"] """

        try:
            user = db.session.query(User).filter(User.user_id == 1).first()
        except Exception as e:
            abort(500, description="Error Retrieving Data")

        temp_data = {
            "email": user.email,
            "password": user.password,
            "role_id": user.role_id,
            "user_id": user.user_id,
        }

        # TODO: Pass actual data
        response = auth_service.login(temp_data)

        if response["success"]:
            return jsonify(response), 200
        elif response["error"] == "Invalid Credentials":
            return jsonify(response), 401
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
        data = request.get_json()
        # Validations -> abort(400, description="Missing Data")

        response = auth_service.logout(data)

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500


@auth_blueprint.route("/roles", methods=["GET"])
@jwt_required()
def get_roles():
    """
    Get all roles.

    @return (dict, int): The response and status code.
    """
    if request.method == "GET":

        # Validations -> abort(400, description="Missing Data")        

        response = auth_service.get_roles()

        if response["success"]:
            return jsonify(response), 200
        else:
            return jsonify(response), 500

