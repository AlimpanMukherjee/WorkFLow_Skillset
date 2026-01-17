age=int(input("enter your age"))
if age<18:
    raise Exception("age is less than 18")
else :
    print("Eligible to vote")