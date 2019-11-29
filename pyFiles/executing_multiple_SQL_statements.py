import sqlite3

path = "Ch14 - Working with Databases/test_database.db"

people_values = (
    ("Mario", "Mario", 40),
    ("Luigi", "Mario", 39),
    ("Brandon", "Fraser", 61)
)

with sqlite3.connect(path) as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """
            DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );
                INSERT INTO People VALUES(
                'Ron',
                'Obvious',
                42
            );
        """
    )
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
