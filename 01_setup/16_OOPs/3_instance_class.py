class Employee:
    company="Google" #this is class attribute
    def __init__(self,name,salary,bond,company):
        self.name=name
        self.salary=salary
        self.bond=bond
        self.company=company

    def getsalary(self):
        return self.salary
    
    def getinfo(self):
        print(f"name : {self.name} , salary : {self.salary} , company : {self.company}")

e=Employee("alimpan",3400000,2,"Tesla") 
print(e.company) #will always print the instance attribute
print(Employee.company) #will always print the class attribute