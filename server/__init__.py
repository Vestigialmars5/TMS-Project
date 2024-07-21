# Import necessary modules
import os
from flask import Flask
from flask_cors import CORS
from .config import Config
from flask_jwt_extended import JWTManager

# Create the application instance
def create_app(config_class=Config):
    # Create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Logs


    # Enable CORS
    CORS(app)

    # Initialize JWT
    jwt = JWTManager()
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
