class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self,p):
        return Point((self.x+p.x),(self.y+p.y))
    
    def printPoint(self):
       print(f"x is {self.x} and y is {self.y}")

    def __add__(self,p):
        return Point((self.x+p.x),(self.y+p.y))


p1=Point(3,2)
p2=Point(6,3)
p1.printPoint()


p=p1.sum(p2) #returns a new point which is sum of p1 and p2
p.printPoint()


pnew=p1+p2 #the + function is overloaded
pnew.printPoint()