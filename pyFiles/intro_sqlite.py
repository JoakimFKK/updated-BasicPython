import sqlite3

"""kigger efter "test_database.db", og hvis den ikke findes bliver den oprettet:
connection = sqlite3.connect("test_database.db")
"""

"""Laver en midlertidligt database:
connection = sqlite3.connect(":memory:")
"""

def ugly_way():
    connection = sqlite3.connect(":memory:")
    query = "SELECT datetime('now', 'localtime');"
    # cursor er et objekt der henter resultater fra en database, en række ad gangen.
    cursor = connection.cursor()
    # fetchone returnere en tuple der indeholder den første række af resultater
    print(cursor.execute(query).fetchone()[0])
    connection.close()

def neat_way():
    with sqlite3.connect(":memory:") as connection:
        cursor = connection.cursor()
        query = "SELECT datetime('now', 'localtime');"
        time = cursor.execute(query).fetchone()[0]
    print(time)