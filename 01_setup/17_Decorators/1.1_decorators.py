#the previous code can be written using this way

def decorators(func):
    def Wrapper():
        print("I am about to print Hello")
        func()
        print("I have exected Hello")
    return Wrapper
    
@decorators
def say_hello():
    print("Hello")

say_hello()