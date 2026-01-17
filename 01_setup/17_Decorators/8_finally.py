a=int(input("enter the number 1 "))
b=int(input("Enter the 2nd number "))

try:
    q=a/b
    print( q)

except Exception as e:
    print( e)

finally:
    print("always executed")