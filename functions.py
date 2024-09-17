# parameters are placeholders in the function definition
# arguments are the actual values
# you define the function using the def keyword
# return keyword is used to return a value from a function,when you don't use return,the output is just null
# you can pass default arguments .....def(name="Brian")
# you can pass any number of arguments using *args and key value pair arguments using **kwargs---keyword arguments
# lambda functions are small quick functions that can be written on one line without needing a name or the def keyword

def hello_brian(name):
    print("Hello"+ " "+ name)

hello_brian("Brian")

def capital_city(city="Nairobi"):
    print(city)

capital_city()

def capital_city(city="Nairobi"):
    print(city)

capital_city("Cairo")


def names(*args):
    print(args)

names("Bruce","Alfred","Gordon","Harvey","Cat")

def countries(*args):
    for country in args:
        print(args)

countries({"country":"Kenya","city":"Nairobi"},{"country":"Tanzania","city":"Darresalam"})

def countries(**kwargs):
    print(kwargs)

countries(country="Kenya",city="Nairobi",country2="Tanzania",city2="Darresalam")