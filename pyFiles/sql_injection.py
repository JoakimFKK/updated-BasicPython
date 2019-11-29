import sqlite3

path = "Ch14 - Working with Databases/test_database.db"

first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
data = (first_name, last_name, age)

with sqlite3.connect(path) as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data)
    cursor.execute(
        "UPDATE People SET Age=? WHERE FirstName=?;",
        (69, "Mario")
    )