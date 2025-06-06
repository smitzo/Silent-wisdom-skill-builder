import datetime
import sqlite3
import random
# Function to create the database and tables

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Create the Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            age INTEGER,
            contact TEXT,
            city TEXT,
            email TEXT PRIMARY KEY,
            password TEXT
        )
    ''')

    # Create the Modules table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS modules (
            category TEXT,
            module_id INTEGER PRIMARY KEY,
            attempts INTEGER
        )
    ''')

    # Create the Gameplay table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gameplay (
            user_id INTEGER,
            time_stamp TIMESTAMP PRIMARY KEY,
            score INTEGER,
            module_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (module_id) REFERENCES modules(module_id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

create_database()