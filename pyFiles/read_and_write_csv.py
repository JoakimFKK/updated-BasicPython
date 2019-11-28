import os
import csv

path = "Test Folder"

def read_csv():
    with open(os.path.join(path, "wonka.csv"), "r") as my_file:
        reader = csv.reader(my_file, delimiter=",")
        # for at undgå toplinjen
        next(reader)
        for first_name, last_name, reward in reader:
            print(f"{first_name} {last_name} got {reward}")

def write_csv():
    ratings = [
        ["Dumbo", "0"],
        ["Two and a Half Men", "10"],
        ["Se7en", "0"]
    ]
    with open(os.path.join(path, "movies.csv"), "w") as my_file:
        writer = csv.writer(my_file)
        writer.writerow(["Movie", ["Rating"]])
        writer.writerow(["Joker","10"])
        writer.writerow(["White Chicks", "10"])
        writer.writerow(["Citizen Kane", "0"])
        writer.writerows(ratings)
