###################################################################################################
# program-flow.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: How does the flow of the code work
#
# Examples of how the control flows through a python program with functions
#######################################################################################################


def first_function():
    print("We're in the first function here")
    score = score + 1
    print(score)


def second_function(name):
    print("Hello", name, "we're in the second function")
    long_name = "Mr " + name


def third_function():
    print("In function 3 now")


def main():
    second_function("Dave")
    third_function()
    first_function()
    third_function()
    second_function("Alan")

score = 5
main()
#####################################################################################################
#   NO CODE BELOW THIS POINT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#####################################################################################################
