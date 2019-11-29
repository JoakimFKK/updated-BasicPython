import sqlite3

roster_list = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
)

with sqlite3.connect(":memory:") as db:
    cursor = db.cursor()
    cursor.executescript(
        """
            CREATE TABLE Roster(
                Name TEXT,
                Species TEXT,
                IQ INT
                );
        """
    )
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", roster_list)
    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]} - {row[2]}")
    print("\n")
    cursor.execute(
        "UPDATE Roster SET Species=? WHERE Name=?;",
        ('Human', "Korben Dallas")
        )

    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]} - {row[2]}")