import sqlite3 as sql
from flask import current_app, g
import click
import os


# Establish db connection, returns db connection from g
def get_db(row=True):
    # Create a connection if doesn't exist
    if "db" not in g:
        db_path = os.path.join(
            current_app.instance_path, current_app.config["DATABASE_URL"].replace(
                "sqlite:///", "")
        )
        g.db = sql.connect(
            db_path,
            detect_types=sql.PARSE_DECLTYPES
        )

        if row:
            # Set queries to return Row objects
            g.db.row_factory = sql.Row
    return g.db


def get_wms_db():
    if "wms_db" not in g:
        wms_db_path = os.path.join(
            current_app.instance_path, current_app.config["WMS_DATABASE_URL"].replace(
                "sqlite:///", "")
        )
        g.wms_db = sql.connect(
            wms_db_path,
            detect_types=sql.PARSE_DECLTYPES
        )

        g.wms_db.row_factory = sql.Row
    return g.wms_db


def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

    wms_db = g.pop("wms_db", None)
    if wms_db is not None:
        wms_db.close()


def init_db():
    tms_db = get_db()
    wms_db = get_wms_db()

    with current_app.open_resource("./models/reset_tms.sql") as f:
        tms_db.executescript(f.read().decode("utf8"))

    with current_app.open_resource("./models/reset_wms.sql") as f:
        wms_db.executescript(f.read().decode("utf8"))


@click.command(name="init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
