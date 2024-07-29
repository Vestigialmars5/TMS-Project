from flask import current_app
from .extensions import db
from .models.tms_models import *
from .models.wms_models import *
from .models.base import Base1, Base2
import click

def init_db():
    with current_app.app_context():
        print("Creating dbs")
        print(f"tms db is being created at {db.get_engine(current_app, bind=None)}")
        print(f"wms db is being created at {db.get_engine(current_app, bind='wms')}")
        Base1.metadata.create_all(bind=db.get_engine(current_app, bind=None))
        Base2.metadata.create_all(bind=db.get_engine(current_app, bind='wms'))

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")

def populate_db():
    with current_app.app_context():
        roles = ["Admin", "Transportation Manager", "Carrier", "Customer/Shipper", "Driver", "Finance/Accounting", "Warehouse Manager"]
        for role in roles:
            db.session.add(Role(role_name=role))
        db.session.commit()

        # Add admin
        admin = User(username="admin", email="admin@gmail.com", password="asdfasdf", role_id=1)
        db.session.add(admin)
        db.session.commit()


@click.command("populate-db")
def populate_db_command():
    populate_db()
    click.echo("Populated the database.")

def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)