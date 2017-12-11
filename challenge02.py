######################################################################################################
# challenge02.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Challenge 02
#
# Add a feature that will guess the user's age then display the following message, "Hello name. Since
# you were born in the year 2001, I think you are 16 years old"
#######################################################################################################

name = input("Please enter your name: ")
year = input("Please enter the year you were born: ")

year = int(year)
age = 2017 - year
# The + sign is used to concatenate the name with the following string, so that the space isn't
# added in before the .
print("Hello", name + ". Since you were born in the year", year, "I think you are", age, "years old")