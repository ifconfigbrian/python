# A lambda function is a small, anonymous function in Python that you can write in a single line

# lambda arguments : expression

# lambda: This is the keyword used to define a lambda function.
# arguments: These are the inputs (just like parameters in a normal function).
# expression: This is what gets returned (it can only be a single expression, no multiple statements).


add = lambda x,y: x+ y

print(add(2,3))


numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
