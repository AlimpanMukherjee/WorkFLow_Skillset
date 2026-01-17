from logging import exception


a=int(input("enter the 1st number :"))

b=int(input("enter the 2nd number :"))

print("Press '+' for Addition")
print("Press '-' for Subtraction")
print("Press '*' for Multiplication")
print("Press '/' for Division")

operation = input("Enter the operation you want to perform: ")
match operation:
    case '+':
        print(f"the sum of {a} and {b} is {a+b}")
    case '-':
        print(f"the difference of {a} and {b} is {a-b}")
    case '*':
        print(f"the product of {a} and {b} is {a*b}")
    case '/': 
        try:
            print(f"the division of {a} and {b} is {a/b}")
        except exception as e:
            print("cannot divide by 0")
    case _:
        print("Invalid operation")
          
    