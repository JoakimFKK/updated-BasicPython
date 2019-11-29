def bad_way_of_using_open():
    input_file = open("hello.txt", "r")

    # Læser teksten direkte som det var skrevet.
    print(input_file.readlines())
    print("\n\n\n")

    # end="" changes behavior at the end from "\n" to ""
    for line in input_file.readlines():
        print(line, end="")

    input_file.close()

    line = input_file.readline()
    while line != "":
        print(line, end="")
        line = input_file.readline() # Read the next line

    input_file.close()


def python_version_of_c_sharp_using():
    with open("hello.txt", "r") as input_file:
        for line in input_file.readlines():
            print(line, end="")