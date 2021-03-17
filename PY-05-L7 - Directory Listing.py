import os
import sys

line = "<------------------------------------------------------------>"

system = sys.platform
print("You are using {}".format(system))

root_folder = input("Enter folder: ")

def mapper(path):
    try:
        for item in os.listdir(path):
            full_path = r"{}\{}".format(path, item)
            if os.listdir(path):
                size = os.stat(full_path).st_size
                print("Found {} -> weighs {} bytes.".format(full_path, size))
            elif os.path.isdir(full_path):
                print("{}\nEntering folder {}\n{}".format(line, item, line))
                mapper(full_path)
            else:
                print("Unknown.")
    except Exception as error:
        print(error)

mapper(root_folder)