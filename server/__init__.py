# Import necessary modules
import os
from flask import Flask
from flask_cors import CORS
from .config import Config
from .jwt_config import jwt
from dotenv import load_dotenv

load_dotenv()

# Create the application instance
def create_app(config_class=Config):
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Environment variables
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 86400
    app.config["JWT_ALGORITHM"] = "HS256"

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Enable CORS
    CORS(app)

    # Initialize JWT
    jwt.init_app(app)

    # Initialize the databases
    from . import db
    db.init_app(app)
    

    # Register blueprints
    from .api.errors_handler import errors_blueprint
    from .api.auth import auth_blueprint
    from .api.admin import admin_blueprint
    from .api.onboarding import onboarding_blueprint
    from .wms.wms import wms_blueprint

    app.register_blueprint(errors_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(onboarding_blueprint)
    app.register_blueprint(wms_blueprint)

    # Return the app
    return app
