# def isGreaterThan9(a):
#     if a>9:
#         return True
#     else:
#         return False
    
numbers=[1,4,2,78,6,43,7,2,32]
#new=list(filter(isGreaterThan9,numbers))
new=list(filter(lambda x:x>9,numbers))
print(new)