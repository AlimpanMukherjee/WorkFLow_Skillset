# a=5
# table=[]

# for i in range(1,11):
#     table.append(a*i)

# print(table)

###### the abobe method is correct but it can also be done in much shorter way#######

table=[5*i for i in range(1,11)]
print(table)

squares=[x*x for x in range (1,11)]
print(squares)

newlist=[1,2,3,4,5,6,7,8,9]
newlist2=[x for x in newlist if x%2==0]
print(newlist2)