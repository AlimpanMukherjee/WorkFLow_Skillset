class Animal:
    location="australlia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("generic  sound")

class Dog(Animal):
    def speak(self):
        super().speak() #this will call the speak method of the parent class as well
        print("woof")

# A=Animal("Goofy")
# A.speak( )

D=Dog("Goofy")
print(D.location)
print(D.name)
D.speak()