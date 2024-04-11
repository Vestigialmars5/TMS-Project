import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("tms_database.db")
cursor = conn.cursor()

# Define SQL CREATE TABLE statements for each model
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

create_carriers_table = """
CREATE TABLE IF NOT EXISTS carriers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    contact_name TEXT,
    contact_email TEXT,
    contact_phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT
);
"""

create_shipments_table = """
CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    weight REAL,
    status TEXT DEFAULT 'pending',
    user_id INTEGER,
    carrier_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (carrier_id) REFERENCES carriers (id)
);
"""

create_invoices_table = """
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY,
    invoice_number TEXT,
    total_amount REAL,
    due_date TEXT,
    status TEXT DEFAULT 'unpaid',
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Execute table creation statements
cursor.execute(create_users_table)
cursor.execute(create_carriers_table)
cursor.execute(create_shipments_table)
cursor.execute(create_invoices_table)

# Commit changes and close connection
conn.commit()
conn.close()
