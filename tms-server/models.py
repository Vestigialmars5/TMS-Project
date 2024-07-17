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

create_driver_details_table = """
CREATE TABLE IF NOT EXISTS driver_details (
    driver_detail_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    license_number TEXT NOT NULL UNIQUE,
    license_expiry DATE NOT NULL,
    vehicle_id INTEGER NOT NULL,
    driver_status TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
"""

create_vehicles_table = """
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY,
    vehicle_plate TEXT NOT NULL UNIQUE,
    vehicle_type TEXT NOT NULL,
    fuel_capacity REAL NOT NULL CHECK (fuel_capacity >= 0),
    litres_per_100km REAL NOT NULL CHECK (litres_per_100km >= 0),
    tonnage REAL NOT NULL CHECK (tonnage >= 0),
    volume REAL NOT NULL CHECK (volume >= 0)
);
"""

create_warehouses_table = """
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL,
    location TEXT NOT NULL,
    docks INTEGER NOT NULL CHECK (docks >= 1),
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES users(user_id)
);
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    order_uuid TEXT NOT NULL UNIQUE,
    customer_id INTEGER,
    order_status TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES users(user_id)
);
"""

create_order_details_table = """
CREATE TABLE IF NOT EXISTS order_details (
    order_detail_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    product_name TEXT NOT NULL,
    priority INTEGER NOT NULL CHECK (priority >= 1),
    quantity INTEGER NOT NULL CHECK (quantity >= 1),
    total_weight REAL NOT NULL CHECK (total_weight >= 0),
    total_volume REAL NOT NULL CHECK (total_volume >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
"""

create_shipments_table = """
CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    customer_id INTEGER,
    driver_id INTEGER,
    warehouse_id INTEGER,
    status TEXT NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (customer_id) REFERENCES users(user_id),
    FOREIGN KEY (driver_id) REFERENCES users(user_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
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
cursor.execute(create_orders_table)
cursor.execute(create_invoices_table)
cursor.execute(create_payments_table)
cursor.execute(create_audit_logs_table)
cursor.execute(create_reports_table)

# Commit changes and close connection
conn.commit()
conn.close()
