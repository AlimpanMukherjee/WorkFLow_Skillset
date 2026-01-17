from functools import reduce
 
def sum(a,b):
    return a+b

numbers=[1,4,2,78,6,43,7,2,32]
c=reduce(sum,numbers)
print(c)