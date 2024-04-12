# ADMIN (permision to everything, managing accounts, system config, performance)
# EDIT DATABSE
# ADD USERS
# DELETE ACCOUNTS
# ACCESS TO LOGS

from flask import redirect, session, g
import sqlite3 as sql
from functools import wraps
import datetime
import requests
import xml.etree.ElementTree as ET


# Establish db connection, returns db connection from g
def get_db():
    # Create a connection if doesn't exist
    if "db" not in g:
        g.db = sql.connect("one_life.db")

        # Set queries to return Row objects
        g.db.row_factory = sql.Row
    return g.db

# Define login_required decorator, redirects to login if not logged in 
""" Change per user """
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id"):
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    return decorated_function


""" ORGANIZE BELOW """


# Transportation Manager (panning, scheduling, executing functionalities)
# Roles: Responsible for managing transportation operations, including route planning, carrier selection, freight management, tracking shipments, and optimizing transportation costs.

# Carrier
# Permissions: Limited access focused on carrier-specific tasks such as accepting/rejecting shipments, updating shipment statuses, and providing freight quotes.
# Roles: Carriers interact with the system primarily to handle assigned shipments, update shipment information, and communicate with the transportation manager regarding delivery status and issues.

# Customer/Shipper
# Permissions: Limited access to functionalities related to creating and tracking shipments, viewing shipment history, and generating reports.
# Roles: Customers or shippers use the system to initiate shipments, track delivery progress, manage billing and invoicing, and generate performance reports.

# Driver
# Permissions: Limited access focused on tasks such as viewing assigned shipments, updating delivery statuses, and communicating with the transportation manager.
# Roles: Drivers interact with the system to receive shipment details, update their availability, report delays or issues, provide real-time location updates, and confirm delivery completion.

# Finance/Accounting
# Permissions: Access to financial modules for managing billing, invoicing, payment processing, and financial reporting.
# Roles: Responsible for billing customers, processing payments to carriers, reconciling invoices, generating financial reports, and ensuring compliance with financial regulations.

# Warehouse/Inventory Manager
# Permissions: Access to inventory management functionalities within the TMS, including inventory tracking, stock replenishment, warehouse allocation, and order fulfillment.
# Roles: Responsible for managing warehouse operations, optimizing inventory levels, coordinating with transportation for inbound and outbound shipments, and ensuring accurate stockkeeping.
