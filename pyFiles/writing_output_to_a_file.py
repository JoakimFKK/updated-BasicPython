"""
mode is an optional string that specifies the mode in which the file is opened.
It defaults to 'r' which means open for reading in text mode.
Other common values are 'w' for writing (truncating the file if it already exists),
'x' for creating and writing to a new file, and 'a' for appending (which on some Unix systems,
means that all writes append to the end of the file regardless of the current seek position).
open(filename, mode)
"""
# Overwrites existing text
# w = Write
output_file = open("hello.txt", "w")
output_file.writelines("I thought what I'd do was, I'd pretend to be one of those deaf-mutes.\n\t- J. D. Salinger\n\n")

lines_to_write = [
    "Veni, vidi, vici",
    "\nI came",
    "\nI saw",
    "\nI conquered"
]
output_file.writelines(lines_to_write)

output_file.close()

# a = Appends
output_file = open("hello.txt", "a")
output_file.writelines("\n\t- Some Dork")
output_file.close()