from flask import Flask, g
from routing.admin import admin_blueprint
from routing.auth import auth_blueprint


app = Flask(__name__)


# Close db connection after every request
@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        print("closing db connection")
        g.db.close()


# Register blueprints
app.register_blueprint(admin_blueprint)
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
