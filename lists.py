users = ['Brian','Bruce','Jane','John']

print(users)

print(users[3])

print(users[-1:4])

empty = []

print('Brian' in empty)
# returns false
empty.insert(0,'Faith')
print(empty)

users.remove("Brian")
print(users)

print(users.pop())
print(users)

users.clear()
print(users)