from flask import Flask, g
from routing.admin import admin_blueprint


app = Flask(__name__)


# Close db connection after every request
@app.teardown_appcontext
def close_db(exception):
    if "db" in g:
        g.db.close()


# Register blueprints
app.register_blueprint(admin_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
