from flask import current_app
from .extensions import db
from .models.tms_models import *
from .models.wms_models import *
from .models.base import Base1, Base2
import click
from werkzeug.security import generate_password_hash
import tests.consts as consts


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
        roles = ["Admin", "Transportation Manager", "Carrier",
                 "Customer/Shipper", "Driver", "Finance/Accounting", "Warehouse Manager"]
        for role in roles:
            db.session.add(Role(role_name=role))
        db.session.commit()

        if development:
            # Add admin
            admin_password = generate_password_hash("asdfasdf")
            admin = User(username="admin", email="admin@gmail.com", password=admin_password, role_id=1, status="inactive")
            db.session.add(admin)
            db.session.commit()

            admin_details = UserDetails(user_id=admin.user_id, first_name="Admin",
                                        last_name="Admin", phone_number="1234567890", address="123 Admin St.")
            db.session.add(admin_details)
            db.session.commit()
        elif testing:
            # Add a user with complete details
            complete_user = User(username=consts.COMPLETE_USER_USERNAME, email=consts.COMPLETE_USER_EMAIL, password=generate_password_hash(consts.COMPLETE_USER_PASSWORD), role_id=consts.COMPLETE_USER_ROLE_ID, status="inactive")
            db.session.add(complete_user)
            db.session.commit()

            complete_user_details = UserDetails(user_id=complete_user.user_id, first_name=consts.COMPLETE_USER_FIRST_NAME, last_name=consts.COMPLETE_USER_LAST_NAME, phone_number=consts.COMPLETE_USER_PHONE_NUMBER, address=consts.COMPLETE_USER_ADDRESS)
            db.session.add(complete_user_details)
            db.session.commit()

            # Add an incomplete user
            incomplete_user = User(username=consts.INCOMPLETE_USER_USERNAME, email=consts.INCOMPLETE_USER_EMAIL, password=generate_password_hash(consts.INCOMPLETE_USER_PASSWORD), role_id=consts.INCOMPLETE_USER_ROLE_ID, status="inactive")
            db.session.add(incomplete_user)
            db.session.commit()
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
