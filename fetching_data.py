import sqlite3
def check_categories():
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Query to select all categories from the Modules table
    cursor.execute("SELECT category FROM modules")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the list of categories
    print("Existing Categories:")
    for row in rows:
        print(row[0])

    # Close the connection
    conn.close()

check_categories()