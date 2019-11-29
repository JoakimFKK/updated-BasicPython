import sqlite3

def ugly_way():
    connection = sqlite3.connect("Ch14 - Working with Databases/test_database.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );"""
    )
    cursor.execute(
        """ INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
        );"""
    )
    connection.commit()
    connection.close()

def neat_way():
    with sqlite3.connect("Ch14 - Working with Databases/test_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );"""
        )
        cursor.execute(
            """ INSERT INTO People VALUES(
                'Ron',
                'Obvious',
                42
            );"""
        )
