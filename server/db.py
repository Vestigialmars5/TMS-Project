import sqlite3 as sql
from flask import current_app, g
import click


# Establish db connection, returns db connection from g
def get_db(row=True, db_name="tms_database.db"):
    # Create a connection if doesn't exist
    if "db" not in g:
        g.db = sql.connect(db_name)

        if row:
            # Set queries to return Row objects
            g.db.row_factory = sql.Row
    return g.db


def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    tms_db = get_db()

    """ wms_db = get_db(db_name="wms_database.db") """
    with current_app.open_resource("./models/reset_tms.sql") as f:
        tms_db.executescript(f.read().decode("utf8"))

    """ with current_app.open_resource("./models/wms_schema.sql") as f:
        wms_db.executescript(f.read().decode("utf8")) """


@click.command(name="init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
