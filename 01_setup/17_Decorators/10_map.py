# def sq(x):
#     return x*x
numbers=[1,4,2,78,6,43,7,2,32]
#new=list(map(sq,numbers))
new=list(map(lambda x:x*x,numbers))
print(new)