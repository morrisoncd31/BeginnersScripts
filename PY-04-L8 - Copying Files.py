import os
#file system may differ b/w op. systems
try:
    os.mkdir(r"C:\Users\Charlie\Downloads\Cars")
except:
    print("This directory already exists.")
with open(r"C:\Users\Charlie\Downloads\Cars\Mustang.txt", "a+") as file:
   pass

path = input("Enter directory path: ")
file_name = input("Enter file name: ")
new_name = input("Enter a new name: ")

os.system(r"copy {}\{} {}\{}".format(path, file_name, path, new_name))