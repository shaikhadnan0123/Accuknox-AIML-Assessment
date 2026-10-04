import csv
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# Read CSV and insert users
with open("data/users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO users (name, email)
            VALUES (?, ?)
        """, (row["name"], row["email"]))

# Save changes
connection.commit()

# Retrieve inserted data
cursor.execute("SELECT id, name, email FROM users")

users = cursor.fetchall()

print("Users stored in database:")

for user in users:
    print(user)

# Close database connection
connection.close()