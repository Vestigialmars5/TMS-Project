# Import necessary modules
import os
from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import jwt, db, migrate


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

    # Enable CORS
    CORS(app)

    # Initialize the extensions
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register commands
    from .db_initiator import init_db_command, populate_db_command
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)

    with app.app_context():
        from .models import tms_models
        from .models import wms_models

    # Register blueprints
    from .api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    """from .api.errors_handler import errors_blueprint
    from .api.admin import admin_blueprint
    from .api.onboarding import onboarding_blueprint
    from .wms.wms import wms_blueprint

    app.register_blueprint(errors_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(onboarding_blueprint)
    app.register_blueprint(wms_blueprint) """

    # Return the app
    return app
