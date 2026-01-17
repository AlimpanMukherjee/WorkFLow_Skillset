def sum(a,b):
    print("i am summing")
    c=a+b
    global z # this will refer to the global variable z and not create a local variable so we can update local variable inside a function but we need to usethe key word local
    z=9 
    return c

z=7
print(sum(8,6))
print(z)
