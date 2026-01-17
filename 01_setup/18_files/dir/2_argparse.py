import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

# Add all arguments BEFORE parsing
parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operation", choices=["add", "sub", "div", "mul"], help="operation to perform")

args = parser.parse_args()  

# Perform calculation
if args.operation == "add":
    print(f"The result is {args.num1 + args.num2}")

elif args.operation == "sub":
    print(f"The result is {args.num1 - args.num2}")

elif args.operation == "mul":
    print(f"The result is {args.num1 * args.num2}")

elif args.operation == "div":
    print(f"The result is {args.num1 / args.num2}")
