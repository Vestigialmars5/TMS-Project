""" from flask import Flask, g
from flask_cors import CORS
import secrets
from api.errors_handler import errors_blueprint
from api.auth import auth_blueprint
from api.onboarding import onboarding_blueprint
from api.admin import admin_blueprint
from wms.wms import wms_blueprint
from jwt_config import jwt


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config["JWT_SECRET_KEY"] = secrets.token_hex(32)
app.config["JWT_ALGORITHM"] = "HS256"
jwt.init_app(app)

CORS(app)

# Close db connection after every request
@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()
        print("closed db connection")


# Register blueprints
app.register_blueprint(errors_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(onboarding_blueprint)
app.register_blueprint(admin_blueprint)

app.register_blueprint(wms_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
 """