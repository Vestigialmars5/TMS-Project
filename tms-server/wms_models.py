import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("wms.db")
cursor = conn.cursor()

# Define SQL CREATE TABLE statements for each model
create_orders_placed_table = """
CREATE TABLE IF NOT EXISTS orders_placed (
    order_id INTEGER PRIMARY KEY,
    order_uuid TEXT NOT NULL UNIQUE,
    warehouse_id INTEGER NOT NULL,
    total_weight REAL NOT NULL,
    total_volume REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_order_products_table = """
CREATE TABLE IF NOT EXISTS order_products (
    order_product_id INTEGER PRIMARY KEY,
    order_id TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    supplier_id INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    weight REAL NOT NULL,
    volume REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders_placed(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
"""

# Execute CREATE TABLE statements
cursor.execute(create_orders_placed_table)
cursor.execute(create_order_products_table)

# Commit changes and close connection
conn.commit()
conn.close()

