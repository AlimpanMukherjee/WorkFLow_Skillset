class Employee:
    company = "hp"
    def getsalary(self):  #self references to the object that is being created
        return 34000
    
e=Employee()
print(e.getsalary())

e2=Employee()
print(e2.getsalary())
print(e.company)