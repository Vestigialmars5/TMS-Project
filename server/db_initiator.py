from flask import current_app
from .extensions import db
from .models.tms_models import *
from .models.wms_models import *
import click


def init_db():
    with current_app.app_context():
        print("Creating dbs")
        print(f"tms db is being created at {db.get_engine(current_app, bind=None)}")
        print(f"wms db is being created at {db.get_engine(current_app, bind='wms')}")
        db.create_all(bind_key=[None, "wms"])

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    app.cli.add_command(init_db_command)