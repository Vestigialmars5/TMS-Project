import sqlite3
from datetime import datetime
from simulation.db import get_db

def create_simulation_event(event_time, event_type, description=""):
    db = get_db()
    db.execute(
        "INSERT INTO simulation_events (event_time, event_type, event_description) VALUES (?, ?, ?)",
        (event_time, event_type, description),
    )
    db.commit()
    db.close()

def get_simulation_event(event_id):
    db = get_db()
    res = db.execute(
        "SELECT * FROM simulation_events WHERE event_id = ?", (event_id,),
    )
    row = res.fetchone()
    db.close()
    return row

def update_simulation_event(event_id, event_time, event_type, description=""):
    db = get_db()
    db.execute(
        "UPDATE simulation_events SET event_time = ?, event_type = ?, event_description = ? WHERE event_id = ?",
        (event_time, event_type, description, event_id),
    )
    db.commit()
    db.close()

def delete_simulation_event(event_id):
    db = get_db()
    db.execute("DELETE FROM simulation_events WHERE event_id = ?", (event_id,))
    db.commit()
    db.close()

def create_event_probability(event_type, probability, average_duration):
    db = get_db()
    db.execute(
        "INSERT INTO event_probabilities (event_type, probability, average_duration) VALUES (?, ?, ?)",
        (event_type, probability, average_duration),
    )
    db.commit()
    db.close()

def get_event_probability(event_type):
    db = get_db()
    res = db.execute(
        "SELECT * FROM event_probabilities WHERE event_type = ?", (event_type,),
    )
    row = res.fetchone()
    db.close()
    return row

def create_driver_event(driver_id, event_type, start_time, end_time, description=""):
    db = get_db()
    db.execute(
        "INSERT INTO driver_events (driver_id, event_type, start_time, end_time, event_description) VALUES (?, ?, ?, ?)",
        (driver_id, event_type, start_time, end_time, description),
    )
    db.commit()
    db.close()

def get_driver_event(event_id):
    db = get_db()
    res = db.execute(
        "SELECT * FROM driver_events WHERE event_id = ?", (event_id,),
    )
    row = res.fetchone()
    db.close()
    return row

def update_driver_event(event_id, driver_id, event_type, start_time, end_time, description=""):
    db = get_db()
    db.execute(
        "UPDATE driver_events SET driver_id = ?, event_type = ?, start_time = ?, end_time = ?, event_description = ? WHERE event_id = ?",
        (driver_id, event_type, start_time, end_time, description, event_id),
    )
    db.commit()
    db.close()

def delete_driver_event(event_id):
    db = get_db()
    db.execute("DELETE FROM driver_events WHERE event_id = ?", (event_id,))
    db.commit()
    db.close()
