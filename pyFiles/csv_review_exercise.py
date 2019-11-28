import csv


path = r"thisCSVFileDoesntExist.csv"

def func_1():
    with open(path, "r") as read_file:
        reader = csv.reader(read_file)
        next(reader)
        for name, pasttime in reader:
            print(f"{name} does {pasttime}.")
            if pasttime.lower().find("fighting") != -1:
                print("FIGHT FIGHT FIGHT ")

def func_2():
    read_path = r"thisCSVFileDoesntExist.csv"
    write_path = r"CATEGORISED_thisCSVFileDoesntExist.csv"

    with open(read_path, "r") as read_file, open(write_path, "w") as write_path:
        reader = csv.reader(read_file)
        writer = csv.writer(write_path)
        writer.writerow(["Name", "Favorite Pastime", "Type of Pastime"])
        for row in reader:
            if row[1].lower().find("fighting") != -1:
                row.append("Combat")
            else:
                row.append("Other")
            writer.writerow(row)