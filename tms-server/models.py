import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tms_database.db")
cursor = conn.cursor()

# Define SQL CREATE TABLE statements for each model
create_roles_table = """
CREATE TABLE IF NOT EXISTS roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT NOT NULL UNIQUE
);
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);
"""

create_user_details_table = """
CREATE TABLE IF NOT EXISTS user_details (
    user_detail_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    address TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""

create_warehouses_table = """
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL,
    location TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES users(user_id)
);
"""

create_shipments_table = """
CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    carrier_id INTEGER,
    warehouse_id INTEGER,
    status TEXT NOT NULL,
    weight REAL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES users(user_id),
    FOREIGN KEY (carrier_id) REFERENCES users(user_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);
"""


create_shipment_statuses_table = """
CREATE TABLE IF NOT EXISTS shipment_statuses (
    status_id INTEGER PRIMARY KEY,
    shipment_id INTEGER,
    status TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);
"""

create_inventory_table = """
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY,
    warehouse_id INTEGER,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    reorder_level INTEGER NOT NULL CHECK (reorder_level >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    shipment_id INTEGER,
    order_status TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES users(user_id),
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);
"""

create_invoices_table = """
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INTEGER PRIMARY KEY,
    shipment_id INTEGER,
    amount REAL NOT NULL CHECK (amount >= 0),
    status TEXT NOT NULL,
    due_date TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);
"""

create_payments_table = """
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    invoice_id INTEGER,
    amount REAL NOT NULL CHECK (amount >= 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id)
);
"""

create_audit_logs_table = """
CREATE TABLE IF NOT EXISTS audit_logs (
    log_id INTEGER PRIMARY KEY,
    id INTEGER,
    action TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT,
    FOREIGN KEY (id) REFERENCES users(user_id)
);
"""

create_reports_table = """
CREATE TABLE IF NOT EXISTS reports (
    report_id INTEGER PRIMARY KEY,
    report_type TEXT NOT NULL,
    generated_by INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data TEXT,
    FOREIGN KEY (generated_by) REFERENCES users(user_id)
);
"""

# Execute table creation statements
cursor.execute(create_roles_table)
cursor.execute(create_users_table)
cursor.execute(create_user_details_table)
cursor.execute(create_warehouses_table)
cursor.execute(create_shipments_table)
cursor.execute(create_shipment_statuses_table)
cursor.execute(create_inventory_table)
cursor.execute(create_orders_table)
cursor.execute(create_invoices_table)
cursor.execute(create_payments_table)
cursor.execute(create_audit_logs_table)
cursor.execute(create_reports_table)

# Commit changes and close connection
conn.commit()
conn.close()
