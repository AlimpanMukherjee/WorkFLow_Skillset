with open("C:/python prog/01_setup/18_files/sam1.txt", "r") as file:
    print(file.read())

with open("C:/python prog/01_setup/18_files/sam1.txt", "r") as file:
    for line in file:
        print(line) # if we write it like this then it will add a new line character after every line
        

with open("C:/python prog/01_setup/18_files/sam1.txt", "r") as file:
    for line in file:
        print(line.strip()) # this will remove the new line character after every line