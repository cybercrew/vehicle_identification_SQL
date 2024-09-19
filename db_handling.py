import sqlite3
import time
import json

def writeToSQL(owner, number, ownerType, entryAllowed):
    db_path = "data.db"
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
    db_path = "data.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query the vehicle_entries table
    cursor.execute('SELECT timeEntered, ownerType, vehicleOwner, vehicleNumber, entryAllowed FROM vehicle_entries')
    rows = cursor.fetchall()
    
    # Convert the rows to a list of dictionaries
    data = []
    for row in rows:
        entry = {
            "timeEntered": row[0],
            "ownerType": row[1],
            "vehicleOwner": row[2],
            "vehicleNumber": row[3],
            "entryAllowed": bool(row[4])
        }
        data.append(entry)
    
    # Close the connection
    conn.close()
    
    return data