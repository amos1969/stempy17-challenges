######################################################################################################
# challenge03.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Challenge 03
#
# Add in some data validation to check that the user is giving a valid year of birth. If they don't,
# make the program continually ask the question until they provide a valid year.
#######################################################################################################

name = input("Please enter your name: ")
# Add some user validation for the year
year_is_valid = False
while not year_is_valid:
    year = input("Please enter the year you were born: ")
    # Check if the input was actually a number
    while not year.isnumeric():
        # If the year wasn't a number run these two lines and check again
        print("Please enter a valid number for the year")
        year = input("Please enter the year you were born: ")
    # The year must have been a number to get this far so convert it
    year = int(year)
    # Make sure the year is a sensible one
    if year > 2017 or year < 1900:
        print("How old are you again?")
    else:
        # If the year is valid, set this variable true to exit the loop
        year_is_valid = True

# Now we can do the calculation
age = 2017 - year
# The + sign is used to concatenate the name with the following string, so that the space isn't
# added in before the .
print("Hello", name + ". Since you were born in the year", year, "I think you are", age, "years old")
