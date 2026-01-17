import os
import shutil

a=os.listdir("C:/python prog/01_setup/18_files/dir")    ##will list all the filesin the dir

print(a)

print(os.getcwd())  #shows the current working directory
print(os.path.exists("C:/python prog/01_setup/18_files/dir"))  #shows if the directory existes or not
# os.remove("C:\python prog/01_setup/18_files\dir\sam1.txt") #this has removed the sam1.txt that was created inside dir
# os.rmdir("18_files/datadir") #this hass removed the datadir that was made inside 18_files
shutil.copy("18_files/sam2.txt", "18_files/sam1.txt",)
shutil.move("18_files/John.txt","C:/python prog/01_setup/18_files/dir") #moves john to dir