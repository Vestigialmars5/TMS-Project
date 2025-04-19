from server.models.tms_models import Role, User, UserDetails
from server.extensions import db
import tests.consts as consts
from werkzeug.security import generate_password_hash


def add_roles():
    roles = ["Admin", "Transportation Manager", "Carrier",
             "Customer/Shipper", "Driver", "Finance/Accounting", "Warehouse Manager"]
    for role in roles:
        db.session.add(Role(role_name=role))
    db.session.commit()


def add_all_roles():
    add_admin()
    # add_transportation_manager()
    add_carrier()
    add_complete_user()
    add_incomplete_user()
    add_incomplete_customer()
    add_customer_shipper()
    # add_driver()
    # add_finance_accounting()
    # add_warehouse_manager()


def add_dev_admin():
    admin_password = generate_password_hash("asdfasdf")
    admin = User(email="admin@gmail.com",
                 password=admin_password, role_id=1, status="inactive")
    db.session.add(admin)
    db.session.commit()

    admin_details = UserDetails(user_id=admin.user_id, first_name="Admin",
                                last_name="Admin", phone_number="1234567890", address="123 Admin St.")
    db.session.add(admin_details)
    db.session.commit()


def add_admin():
    admin_password = generate_password_hash(consts.ADMIN_PASSWORD)
    admin = User(email=consts.ADMIN_EMAIL,
                 password=admin_password, role_id=consts.ADMIN_ROLE_ID, status="inactive")
    db.session.add(admin)
    db.session.commit()

    admin_details = UserDetails(user_id=admin.user_id, first_name=consts.ADMIN_FIRST_NAME,
                                last_name=consts.ADMIN_LAST_NAME, phone_number=consts.ADMIN_PHONE_NUMBER, address=consts.ADMIN_ADDRESS)
    db.session.add(admin_details)
    db.session.commit()


def add_transportation_manager():
    pass


def add_customer_shipper():
    customer_password = generate_password_hash(consts.CUSTOMER_PASSWORD)
    customer = User(email=consts.CUSTOMER_EMAIL,
                            password=customer_password, role_id=consts.CUSTOMER_ROLE_ID, status="inactive")
    db.session.add(customer)
    db.session.commit()

    customer_details = UserDetails(user_id=customer.user_id, first_name=consts.CUSTOMER_FIRST_NAME,
                                           last_name=consts.CUSTOMER_LAST_NAME, phone_number=consts.CUSTOMER_PHONE_NUMBER,
                                           address=consts.CUSTOMER_ADDRESS)
    db.session.add(customer_details)
    db.session.commit()


def add_carrier():
    carrier_password = generate_password_hash(consts.CARRIER_PASSWORD)
    carrier = User(email=consts.CARRIER_EMAIL,
                   password=carrier_password, role_id=consts.CARRIER_ROLE_ID, status="inactive")
    db.session.add(carrier)
    db.session.commit()

    carrier_details = UserDetails(user_id=carrier.user_id, first_name=consts.CARRIER_FIRST_NAME,
                                  last_name=consts.CARRIER_LAST_NAME, phone_number=consts.CARRIER_PHONE_NUMBER, address=consts.CARRIER_ADDRESS)
    db.session.add(carrier_details)
    db.session.commit()


def add_complete_user():
    complete_user_password = generate_password_hash(
        consts.COMPLETE_USER_PASSWORD)
    complete_user = User(email=consts.COMPLETE_USER_EMAIL,
                         password=complete_user_password, role_id=consts.COMPLETE_USER_ROLE_ID, status="inactive")
    db.session.add(complete_user)
    db.session.commit()

    complete_user_details = UserDetails(user_id=complete_user.user_id, first_name=consts.COMPLETE_USER_FIRST_NAME,
                                        last_name=consts.COMPLETE_USER_LAST_NAME, phone_number=consts.COMPLETE_USER_PHONE_NUMBER, address=consts.COMPLETE_USER_ADDRESS)
    db.session.add(complete_user_details)
    db.session.commit()


def add_incomplete_user():
    incomplete_user = User(email=consts.INCOMPLETE_USER_EMAIL, password=generate_password_hash(
        consts.INCOMPLETE_USER_PASSWORD), role_id=consts.INCOMPLETE_USER_ROLE_ID, status="inactive")
    db.session.add(incomplete_user)
    db.session.commit()


def add_incomplete_customer():
    incomplete_customer = User(email=consts.INCOMPLETE_CUSTOMER_EMAIL, password=generate_password_hash(
        consts.INCOMPLETE_CUSTOMER_PASSWORD), role_id=consts.INCOMPLETE_CUSTOMER_ROLE_ID, status="inactive")
    db.session.add(incomplete_customer)
    db.session.commit()

    incomplete_customer_details = UserDetails(user_id=incomplete_customer.user_id, first_name=consts.INCOMPLETE_CUSTOMER_FIRST_NAME,
                                              last_name=consts.INCOMPLETE_CUSTOMER_LAST_NAME, phone_number=consts.INCOMPLETE_CUSTOMER_PHONE_NUMBER, address=consts.INCOMPLETE_CUSTOMER_ADDRESS)
    db.session.add(incomplete_customer_details)
    db.session.commit()
