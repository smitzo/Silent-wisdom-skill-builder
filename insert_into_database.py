import datetime
import sqlite3

def insert_gameplay_data(score, category):
    with open('current.txt', 'r') as file:
        email = file.read()
        
    print(email)
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Execute the INSERT query to insert gameplay data into the gameplay table
    cursor.execute("""
        INSERT INTO gameplay (email, time_stamp, score, category) 
        VALUES (?, ?, ?, ?)
    """, (email, timestamp, score, category))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
