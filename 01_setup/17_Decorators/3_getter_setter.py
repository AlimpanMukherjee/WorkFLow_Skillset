class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def firstname(self):
        l=self.name.split(" ")
        return l[0]
    
    def set_firstname(self,first):
        l=self.name.split(" ")
        new_name=f"{first}{l[1]}"
        self.name=new_name

e=Employee("Jack Doe",34098)
print(e.firstname())
e.set_firstname("john ")
print(e.name)
