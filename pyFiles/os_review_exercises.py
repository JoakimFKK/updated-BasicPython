import os
import glob


path = "Python/Test folder"

def print_all_files_in_a_directory():
    for file in os.listdir(path):
        print(file)

def print_all_files_in_directory_thats_txt():
    g_path = os.path.join(path, "*.txt")
    for g_file in glob.glob(g_path):
        print(g_file)

def walk_through_folder_and_rename_files():
    for current_folder, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(".txt"):
                current_file = os.path.join(current_folder, filename)
                new_filename = current_file[:-4] + "_a.txt"
                os.rename(current_file, new_filename)
                print(os.path.exists(current_file))

    # 5
    if not os.path.exists(os.path.join(path, "Output")):
        os.mkdir(os.path.join(path, "Output"))

    with open(os.path.join(path, "Output", "python.txt"), "w") as writer:
        writer.write("I was put in here by python!")