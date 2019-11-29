input_file = open("hello.txt", "r")
print("Line 0 (first line):", input_file.readline())

input_file.seek(0)
print("Line 0 again:", input_file.readline())
print("Line 1:", input_file.readline())

input_file.seek(8)
print("Line 0 (starting at 9th character):", input_file.readline())

input_file.close()