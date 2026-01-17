with open("C:/python prog/01_setup/18_files/sam1.txt ","r") as file:
    content=file.read()

with open("C:/python prog/01_setup/18_files/sam2.txt","w") as file:
    file.write(content)
    