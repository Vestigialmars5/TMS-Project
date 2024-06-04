import functools

from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

# TODO: check auth libraries


# TODO: check this, copied from flask's official website
@auth_blueprint.route("/Register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@auth_blueprint.route("/Login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@auth_blueprint.route("/CheckLoginCredentials", methods=("GET", "POST"))
def checkLoginCredentials():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # TODO: Remove after finishing up login testing
    print("checkLoginCredentials {")
    print("Email", email)
    print("Password", password)
    print("Sending", jsonify({"success":True}), "200")
    print("}")

    # TODO: Validations between data being passed and from db
    ############

    # Example unsuccessful return jsonify({'success': False, 'error': 'Invalid email or password'}), 401
    return jsonify({"success": True}), 200


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


@auth_blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# Testing for db across files
@auth_blueprint.route("/db_test")
def db_test():
    db = get_db()
    res = db.execute("SELECT * FROM users")
    row = res.fetchone()
    users = dict(row) if row else {}
    return users
