import random

randomnumber=[random.randint(1,20) for i in range(8)]
print(randomnumber)
sortedrandom=sorted(randomnumber)
print(sortedrandom)
sortedesc=sorted(randomnumber,reverse=True)
print(sortedesc)
unique=list(set(randomnumber)) #this just keeps the unique elements in the list
print(unique)   