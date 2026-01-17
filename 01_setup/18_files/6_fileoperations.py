with open("C:/python prog/01_setup/18_files/sam3.txt", "w+") as file:  #w+ opens the file for reading and writing, creating it if it doesn't exist
    file.write("this a w+  file")
    file.write("the file is going to be created")
    file.seek(0)  # Move the file pointer to the beginning of the file
    content = file.read()  # Read the content of the file
    print(content)  # Print the content of the file
