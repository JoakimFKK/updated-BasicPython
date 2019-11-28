import os

path = "folderDelete"
for file in os.listdir(path):
    if os.path.getsize(os.path.join(path, file)) <= 1000:
        os.remove(os.path.join(path, file))
    # print(os.path.getsize(os.path.join(path, file)))