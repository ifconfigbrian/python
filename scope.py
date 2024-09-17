# global variables and functions are accessible from anywhere within the code
# defined on top of the program
# variables defined inside a block or function are only accessible there.....that is local scope
# enclosing scope...when you have a nested function,the inner function can access whatever is in the outer function.....also called non local scope
# built in scope...this contains built in python names,can be used anywhere in your code

# global scope

x = 21

def print_x():
    print(x)

print_x()


# local scope

def my_age():
    age = 22
    print(age)
my_age()


# try to access the age from another function

# def brians_age():
#     print(age)

# brians_age()


# enclosing scope
def outer_function():
    z = 20  # Enclosing variable

    def inner_function():
        print(z)  # Accesses enclosing variable z

    inner_function()  # Output: 20

outer_function()

# built in scope

print(len("Brian"))  # len is a built-in function


