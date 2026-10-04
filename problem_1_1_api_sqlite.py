import requests
import sqlite3

API_URL = "https://openlibrary.org/search.json?q=python&limit=5"

# 1. Fetch data from API
response = requests.get(API_URL, timeout=10)
response.raise_for_status()

data = response.json()
books = data["docs"]

# 2. Connect to SQLite
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# 3. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        publication_year INTEGER
    )
""")
cursor.execute("DELETE FROM books")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        publication_year INTEGER
    )
""")

cursor.execute("DELETE FROM books")
# 4. Insert books
for book in books:
    title = book.get("title")
    authors = ", ".join(book.get("author_name", []))
    publication_year = book.get("first_publish_year")

    cursor.execute("""
        INSERT INTO books (title, author, publication_year)
        VALUES (?, ?, ?)
    """, (title, authors, publication_year))

# 5. Save changes
connection.commit()

# 6. Retrieve and display data
cursor.execute("""
    SELECT title, author, publication_year
    FROM books
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

# 7. Close database connection
connection.close()

