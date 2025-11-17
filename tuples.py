day_pair = ("Monday", 1)

name_age_and_sex = ("Ash", 20, "Male")

fruits = [('banana', 'yellow', 10), ('apple', 'red', 19)]

# Destructuring/Unpacking the tuple with a for loop
for name, color, price in fruits:
    print(name, color, price)

# Unpacking arguments

def add(a, b):
    return a + b

numbers = (1, 2)

print(add(*numbers))