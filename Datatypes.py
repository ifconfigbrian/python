# strings,integers,casting to strings,concatenation,multiline
# literal assignment

first_name = "Bruce"
last_name = "Wayne"
year = 1990
city = "Gotham City"

# print out the datatypes
print(type(first_name))
print(type(last_name))
print(type(year))
print(type(city))

# concatenation

print("My name is " + first_name + " " + last_name)

# casting int to string

print("I was born in the year" + " " + str(year) + "," + city + " "+ "is my Home")


# multiline

multiline = '''

Hey, how are you?                                   

I was just checking in.    
                                All good?



'''
print(multiline)

# escape characters

# new line
print("The Batman\nThe Joker")

# horizontal tab
print("Left tab\tRight tab")

# insert a backslash

print("C:\\Desktop\\")   
# output--- C:\Desktop\

# insert a single quote
print("The joker\'s laughter")

# move the cursor to beginning of the line

print("Romeo and \rJuliet")
# output----Julietand 

# trigger system alert sound
print("This is an alarm\a")

# unicode characters
print("\u03A9")  # Omega symbol (Ω)
print("")

# create a simple menu

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
