# exceptions are errors that occur during program execution
# they are handled in try except blocks to prevent the program from crushing
# the finally block contains code that should run no matter what
# else block runs when no exceptions occur
# you can manually trigger exceptions using the raise keyword
# you can create your own custom exceptions by inheriting from the Exception class
# pass is a placeholder where there should be code but none yet

class CustomError(Exception):
    pass

def check_number(x):
    if x < 0:
        raise CustomError("Cannot be negative!")

try:
    check_number(-1)
except CustomError as e:
    print(e)


try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No errors! The result is:", x)



try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No errors! The result is:", x)
finally:
    print("code that will aways run")