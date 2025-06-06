import sqlite3
# Function to insert categories into the Modules table
def insert_categories():
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # List of categories to insert
    categories = [
        "learning_digit_sign",
        "arithmetic_module",
        "understanding_emotions",
        "animated_stories",
        "interactive_balloon_number_matching",
        "physical_fitness",
        "quiz",
        "reflex_check",
        "keyboard_typing"
    ]

    # Insert each category into the Modules table
    for category in categories:
        cursor.execute(
            "INSERT INTO modules (category, attempts) VALUES (?, 0)", (category,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

insert_categories()