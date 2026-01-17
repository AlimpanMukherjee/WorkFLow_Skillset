name="Alimpan" #strings are immutable,cannot be changed in the memory

#name[0]="R" #this cannot be done , will show runtime error , for other data types it is valid but for strings it is not valid

a=len(name)

print(a)

print(name.upper(),name) #orriginal string remains same (immutable)

print(name.lower())

print(name.capitalize()) #convert the first letter to upper case

print(name.title()) #convert the first letter of every word to upper case

text="   alimpan mukherjee   "

print(text.strip()) #removes the free spaces before the starting and ending

print(text.lstrip()) #remove spaces from the left

print(text.rstrip()) #remove spaces from the right

print(text.find("im"))

print(text.replace("im","yre"))

fruits="Apple,banana,pinapple"

print(fruits.split(","))

print(",".join(['Apple','banana','pinapple']))

mystring="Ali123"
print(mystring.isalpha())
print(mystring.isnumeric())
print(mystring.isalnum())

str1="Alimpan"
str2="Mukherjee"
concat_str=str+" "+str2
print(concat_str)