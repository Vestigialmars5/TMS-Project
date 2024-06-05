from flask import Flask, g
from flask_cors import CORS
import secrets
from routing.admin import admin_blueprint
from routing.auth import auth_blueprint


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

CORS(app)

# Close db connection after every request
@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()
        print("closed db connection")


# Register blueprints
app.register_blueprint(admin_blueprint)
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
