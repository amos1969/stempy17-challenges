######################################################################################################
# challenge04.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Challenge 04
#
# Add a feature where it tells the user an interesting fact based on their age, eg. "Since most humans
# sleep for about a third of their life, that means you have slept for a total of 5 years"
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

# Do integer division to get an integer back (this truncates the answer rather than rounding it)
sleep = age//3
# Break the extra long line over multiple lines, any pythonic object with anything inside brackets
# can be split over multiple lines, where the commas sit.
print("Since most humans sleep for about a third of their life, that means you have slept for a total of",
      sleep, "years")

