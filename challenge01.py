######################################################################################################
# challenge01.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Challenge 01
#
# Develop a system that will ask a user for their name and the year of their birth, then repeat this
# information back to them, by displaying the following message, "Hello name. You were born in the
# year 2001"
######################################################################################################

name = input("Please enter your name: ")
year = input("Please enter the year you were born: ")
# The + sign is used to concatenate the name with the following string, so that the space isn't
# added in before the .
print("Hello", name + ". You were born in the year", year)