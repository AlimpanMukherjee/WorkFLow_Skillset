count = 0         # line count
countword = 0     # word count
countchar = 0     # character count

with open("C:/python prog/01_setup/18_files/sam2.txt", "r") as file:
    for line in file:
        count += 1  # counting lines
        currentword = False
        for ch in line:
            if ch != " " and ch != "\n" and currentword == False:
                countword += 1
                currentword = True
            elif ch == " " or ch == "\n":
                currentword = False
            if ch != " " and ch != "\n":
                countchar += 1

print("Number of lines in the file:", count)
print("Number of words in the file:", countword)
print("Number of characters in the file:", countchar)



