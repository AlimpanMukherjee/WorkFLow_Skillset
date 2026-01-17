class Employee:
    def __init__(self, salary,name, bond):
        self.name=name
        self.salary=salary
        self.bond=bond

    def getSalary(self):
        return self.salary
    
    def getname(self):
        return self.name
    
    def getInfo(self):
        print(f"The employee details are {self.name} and {self.salary} and {self.bond}")
    
e1=Employee(320000,"Alimpan",4)
print(e1.getSalary())
print(e1.getname())
print(e1.getInfo())
