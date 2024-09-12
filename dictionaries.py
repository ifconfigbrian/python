students = {'Brian':21,'John':20,'David':30}

print(students)

# print(students('Joe'))

# using the get method is better because it raises no error if the value is not found

print(students.get('Joe'))

# print the values
print(students.values())

# print key value pairs as tuples
print(students.items())



