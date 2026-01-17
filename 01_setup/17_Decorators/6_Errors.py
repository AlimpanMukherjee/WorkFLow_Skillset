''' if we write the code below 
then there are chances that the code might stop
if any of the user enters anything except int
'''

# while True:
#     a=int(input("Enter the first number"))
#     b=int(input("Enter the second number"))
#     print(f"The sum is {a+b}")


while True:
    try:
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
        print(f"The sum is {a+b}")

    except Exception as e:
        print("some error occured!",e)