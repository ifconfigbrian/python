# while loop

age = 21

while age > 18:
    print("Crack a bottle!!")
    if age > 20:
        break
    age+=1


# second while loop

while age == 21:
    age += 1
    print(age)


# for loops

for x in 'Brian':
    print(x)


names = ['Bruce','Brian','Alfred','Gordon','Stewart']

for n in names:
    print(n)

    print("")

for n in names:
    if n == 'Bruce':
        continue
    print(n)
