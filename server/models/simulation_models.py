import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("simulation_database.db")
cursor = conn.cursor()

# Define SQL CREATE TABLE statements for each model
create_simulation_control_table = """
CREATE TABLE IF NOT EXISTS simulation_control (
    simulation_time DATETIME PRIMARY KEY,
    speed_factor REAL NOT NULL,
    status TEXT NOT NULL
);
"""

create_simulation_events_table = """
CREATE TABLE IF NOT EXISTS simulation_events (
    event_id INTEGER PRIMARY KEY,
    event_time DATETIME NOT NULL,
    event_type TEXT NOT NULL,
    event_description TEXT
);
"""

create_event_probabilities_table = """
CREATE TABLE IF NOT EXISTS event_probabilities (
    event_type TEXT PRIMARY KEY,
    probability REAL NOT NULL,
    average_duration REAL NOT NULL
);
"""

create_warehouses_table = """
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL,
    location TEXT NOT NULL,
    docks INTEGER NOT NULL
);
"""

create_table_inventory = """
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    max_quantity INTEGER NOT NULL,
    reorder_level INTEGER NOT NULL,
    warehouse_id INTEGER,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);
"""

create_table_drivers = """
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY,
    current_location TEXT NOT NULL,
    status TEXT NOT NULL,
    last_update DATETIME NOT NULL,
    risk_factor REAL NOT NULL,
    current_event TEXT NOT NULL,
    license_number TEXT NOT NULL,
    license_expiry_date DATETIME NOT NULL,
    vehicle_id INTEGER NOT NULL,
    route_id INTEGER,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);
"""

create_table_vehicles = """
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY,
    vehicle_type TEXT NOT NULL,
    tonnage REAL NOT NULL,
    volume REAL NOT NULL,
    fuel_capacity REAL NOT NULL,
    status TEXT NOT NULL
);
"""

create_table_routes = """
CREATE TABLE IF NOT EXISTS routes (
    route_id INTEGER PRIMARY KEY,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL,
    waypoints TEXT NOT NULL,
    distance REAL NOT NULL,
    estimated_duration REAL NOT NULL
);
"""

create_table_driver_events = """
CREATE TABLE IF NOT EXISTS driver_events (
    event_id INTEGER PRIMARY KEY,
    driver_id INTEGER,
    event_type TEXT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    event_description TEXT,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);
"""

# Execute table creation statements
cursor.execute(create_simulation_control_table)
cursor.execute(create_simulation_events_table)
cursor.execute(create_event_probabilities_table)
cursor.execute(create_warehouses_table)
cursor.execute(create_table_inventory)
cursor.execute(create_table_drivers)
cursor.execute(create_table_vehicles)
cursor.execute(create_table_routes)
cursor.execute(create_table_driver_events)

# Commit changes and close connection
conn.commit()
conn.close()
