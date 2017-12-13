###################################################################################################
# defining-functions.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Function definitions and how to call them
#
# Examples of how to define and call functions
#######################################################################################################

# Simple function definition
def simple():
    print("Hello we're in the simple function")
    print("We're still in the function here")

# Function definition passing in values
def welcome(name, age):
    print("Hello", name, "welcome to the functions program")
    print("You were", age, "years old")
    print("Happy Birthday!")
    age = age + 1
    return age

# Function definition returning values

# Combining them

# Discuss global vs local variables

the_name = input("Please enter your name: ")
the_age = int(input("Please enter your age: "))
the_age = welcome(the_name, the_age)

print(the_age)

