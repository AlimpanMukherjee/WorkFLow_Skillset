while True:
    try:
        a=int(input("enter the first nunmber"))
        b=int(input("enter the second nunmber"))
        print(f"the result after the division is {a/b}")
    except ValueError:
        print("bad typecaste")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except Exception as e:
        print("Unknown error",e)