import sqlite3
import time
import json


def initialiseTable():
    db_path = "cars.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicle_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timeEntered TEXT,
            ownerType TEXT,
            vehicleOwner TEXT,
            vehicleNumber TEXT,
            entryAllowed BOOLEAN
        )
    ''')

def writeToSQL(owner, number, ownerType, entryAllowed):
    db_path = "cars.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    initialiseTable()
    
    # Insert new data
    new_data = (time.strftime("%H:%M", time.localtime(time.time())), ownerType, owner, number, entryAllowed)
    cursor.execute('''
        INSERT INTO vehicle_entries (timeEntered, ownerType, vehicleOwner, vehicleNumber, entryAllowed)
        VALUES (?, ?, ?, ?, ?)
    ''', new_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def readSQL():
    db_path = "savedcars.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query the vehicle_entries table
    cursor.execute('SELECT vehicleNumber, vehicleOwner, ownerType FROM saved_cars')
    rows = cursor.fetchall()
    
    # Convert the rows to a list of dictionaries
    data = []
    for row in rows:
        entry = {
            "vehicleNumber": row[0],            
            "vehicleOwner": row[1],
            "ownerType": row[2]
        }
        data.append(entry)
    
    # Close the connection
    conn.close()
    
    return data