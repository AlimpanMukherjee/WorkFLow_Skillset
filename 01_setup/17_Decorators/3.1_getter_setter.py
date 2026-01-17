#this is another version of the previous code
class Employee:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name

    @property #now this has become a property
    def firstname(self):
        l=self.name.split(" ")
        return l[0]
    
    @firstname.setter #this is the setter for the property
    def firstname(self,first):
        l=self.name.split(" ")
        new_name=f"{first}{l[1]}"
        self.name=new_name

e=Employee("Jack Doe",78608)
e.firstname="John"
print(e.name)