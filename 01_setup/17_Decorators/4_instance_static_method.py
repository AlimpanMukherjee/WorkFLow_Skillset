class Employee:
    company="hp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #instance method (default)...the method that is created inside the function
    def printinfo(self):
        info= f"Then name is{self.name} and the company is {self.company}"
        print(info)

    @staticmethod #we use the decorator method (static) this will convert the method from instance method to static method...
    #static methos does not use the instance of the class
    def sum(a,b):
        return a+b
    
    @classmethod
    def printCompany(cls):
        print(cls.company)

    #clss methos does not use the instance of the class
    @classmethod
    def changeCompany(cls,newcompany):
        cls.company=newcompany #it can change the value of the cl


e1=Employee("Jack",3455)
e2=Employee("JIll",3455)
print(Employee.company)
#print(Employee.name) # this will throw an error because we dont have name as a class variable
e1.printinfo()
e2.printinfo()
print(e2.sum(3,6))
e2.changeCompany("Acer")
print(Employee.company)