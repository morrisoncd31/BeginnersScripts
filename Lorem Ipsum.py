path = input("Enter a directory path for the text file: ")
filename = input("Enter full filename: ")
# file structure will differ depending on the operating system.
file = open(path+"\\"+filename, "r")
for line in file:
    print(line)

file.close()
