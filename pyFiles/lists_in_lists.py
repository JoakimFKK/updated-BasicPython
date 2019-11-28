# Name, students, tuition
universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000], 
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500]
]
# structure: list = [ [sub_list1], [sub_list2], [sub_list3] ]

def enrollment_stats(x):
    list_students = [[],[]] # Initialises a list, containing two empty lists.
    for n in x:
        list_students[0].append(n[1]) # Contains all universities[n][1] values - Students
        list_students[1].append(n[2]) # Contains all universities[n][2] values - Tuition
    return list_students

def mean(x):
    return sum(x) / len(x)

def median(x):
    x.sort()
    length = len(x)
    if not length % 2:
        return x[(length - 1) / 2]
    return x[int(length / 2)]


foobar = enrollment_stats(universities)
print(f"Total students:\t{sum(foobar[0])}") # Total students: 77285
print(f"Total tuition:\t{sum(foobar[1]):,.2f}") # Total tuition:  271,905.00


print(f"Student Mean:\t{mean(foobar[0]):,.2f}") # Student Mean:   11,040.71
print(f"Studen median:\t{median(foobar[0])}") # Studen median:  10566


print(f"Tuition Mean:\t{mean(foobar[1]):,.2f}") # Tuition Mean:   38,843.57
print(f"Tuition median:\t{median(foobar[1]):,.2f}") # Tuition median: 39,849.00