def decorators(func):
    def Wrapper():
        print("I am about to print Hello")
        func()
        print("I have printed Hello")
    return Wrapper

def say_hello():
    print("🔍hello")


'''
f will look lile
def f():
print("I amabou t to print hello)
print("hello")
print("I have printed hello")
'''
f=decorators(say_hello)
f()


# 🔍 Explanation:
# 1. def decorators(func):
# This defines a function called decorators that takes one argument, func. This argument is expected to be a function (in this case, say_hello).

# 2. def Wrapper():
# Inside the decorators function, you define another function called Wrapper. This is called a nested function or wrapper function. It "wraps around" the original function (func) to add some extra behavior.

# 3. Inside Wrapper():
# python
# Copy code
# print("I am about to print Hello")
# func()  # This calls the original function passed in, i.e., say_hello()
# print("I have printed Hello")
# This means:

# Before calling the original function (say_hello()), it prints a message.

# Then it calls the function (which prints "hello").

# Finally, it prints another message after the call.

# 4. return Wrapper:
# Now, the decorators function returns the Wrapper function, not by calling it (no parentheses), but just the function object. So the function you get back (stored in f) is actually Wrapper, not say_hello directly.

# 5. def say_hello():
# This is a simple function that just prints "hello".

# 6. f = decorators(say_hello):
# You're passing say_hello as an argument to decorators.

# decorators returns the Wrapper function.

# So, now f points to Wrapper.

# 7. f():
# Now, calling f() is the same as calling Wrapper(), which:

# Prints "I am about to print Hello"

# Then calls say_hello() (which prints "hello")

# Then prints "I have printed Hello"