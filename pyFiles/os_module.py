import os
import glob

short_path = r"C:\Users\joak\source\repos\Python"

### create and remove directories
def create_and_remove_dirs(path):
    os.mkdir(os.path.join(path, "New fold"))
    os.rmdir(path + r"\New fold")

### form two strings into a valid path
def form_two_strings_into_a_valid_path():
    path = os.path.join(short_path, "Test folder")
    print(path)

### get list of items in directory.
### And rename if the name ends with "".jpeg"
def see_notes_above(path):
    for file in os.listdir(path):
        if file.lower().endswith(".jpeg"):
            file_path = os.path.join(path, file)
            new_file = file_path[:-5] + ".txt"
            os.rename(file_path, new_file)
    glob_path = os.path.join(path, "*.txt")

    ### Rename files indiscriminately
    for filename in glob.glob(glob_path):
        file_path = os.path.join(path, filename)
        new_filename = file_path[:-4] + "_get.txt"
        os.rename(filename, new_filename)


### Find files in subfolders.
def find_files_in_subfolders():
    sub_path = "C:/Users/joak/source/repos/Python/Test folder"
    get_subdirectories = os.path.join(sub_path, "*/*.txt")
    # Only finds sub1
    for file_name in glob.glob(get_subdirectories):
        print(file_name)

### Checks the existence of files and folders
def see_if_folder_exists():
    path = "C:/Users/joak/source/repos/Python/Test folder"
    files_and_folders = os.listdir(path)

    for folder_name in files_and_folders:
        full_path = os.path.join(path, folder_name)
        if os.path.isdir(full_path):
            os.rename(full_path, full_path + " folder")

def os_walk_method():
    ### Traversing a directory structure
    ### This function returns all the possible combinations of folder,subfolders,
    ###  and filenames as tuples that represents the paths to reach every file anywhere in a named root directory
    path = "C:/Users/joak/source/repos/Python/Test folder"
    for current_folder, subfolders, file_names in os.walk(path):
        for file_name in file_names:
            print(os.path.join(current_folder, file_name))
    ### OUTPUT:
    # # C:/Users/joak/source/repos/Python/Test folder\sub0TXT.txt
    # # C:/Users/joak/source/repos/Python/Test folder\sub1 folder\sub1TXT.txt
    # # C:/Users/joak/source/repos/Python/Test folder\sub2 folder\sub1\sub2TXT.txt
    # # C:/Users/joak/source/repos/Python/Test folder\sub3 folder\sub2\sub1\sub3TXT.txt