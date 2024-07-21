DROP TABLE IF EXISTS order_products;
DROP TABLE IF EXISTS orders_placed;

CREATE TABLE orders_placed (
    order_id INTEGER PRIMARY KEY,
    order_uuid TEXT NOT NULL UNIQUE,
    warehouse_id INTEGER NOT NULL,
    total_weight REAL NOT NULL,
    total_volume REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_products (
    order_product_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
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

