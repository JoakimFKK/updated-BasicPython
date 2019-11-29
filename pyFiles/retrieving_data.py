import sqlite3

path = "Ch14 - Working with Databases/test_database.db"

with sqlite3.connect(path) as connection:
    cursor = connection.cursor()
    cursor.execute(
        "SELECT LastName, FirstName, Age FROM People ORDER BY Age ASC;"
    )
    for row in cursor.fetchall():
        print(row)