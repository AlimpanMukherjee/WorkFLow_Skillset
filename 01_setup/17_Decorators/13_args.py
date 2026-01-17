# def sum(a,b):
#     return a+b

# print(sum(8,9))

#### by args we can pass multiple values to a function and collect it as an iterable ####

def sum(*args):
    print(args)
    total=0
    for item in args:
        total+=item
    return total
    
print(sum(1,8,8,6))

