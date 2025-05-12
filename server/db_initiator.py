from flask import current_app
from .extensions import db
from .models.tms_models import *
from .models.wms_models import *
from .models.base import Base1, Base2
import click
from werkzeug.security import generate_password_hash
import tests.consts as consts
from server.db_populator import *


def init_db():
    with current_app.app_context():
        Base1.metadata.create_all(bind=db.engine)
        Base2.metadata.create_all(bind=db.engines["wms"])


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def populate_db(development=False, testing=False):
    with current_app.app_context():
        # Creates roles
        add_roles()

        if development:
            # Creates an admin for development
            add_dev_admin()
        elif testing:
            # Creates a user for each role for testing plus some other users
            add_all_roles()
        else:
            pass


@click.command("populate-db")
@click.option("--development", is_flag=True, help="Populate the database for development.")
@click.option("--testing", is_flag=True, help="Populate the database for testing.")
def populate_db_command(development, testing):
    if development:
        populate_db(development=True)
        click.echo("Populated the database for development.")
    elif testing:
        populate_db(testing=True)
        click.echo("Populated the database for testing.")
    else:
        populate_db()
        click.echo("Populated the database.")


def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
