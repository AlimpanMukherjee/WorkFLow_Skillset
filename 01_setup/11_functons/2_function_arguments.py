def add(a,b,plus=4): #put the positional arg after the default arg
    x=a+b+plus
    return x

c=add(3,6)
d=add(8,4,5)

print(c)
print(d)