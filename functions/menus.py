###################################################################################################
# menus.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Implement a menu system using functions
#
# How to do a menu system using functions
#######################################################################################################

def main():
    while True:
        print("Welcome to the program")
        print("Please choose from the following options")
        print("A Option 1 (I'd actually put a named option in here")
        print("B Option 2")
        print("C Option 3")
        print("X To exit the program")
        user_choice = input()
        if user_choice.upper() == "A":
            option_a()
        elif user_choice.upper() == "B":
            option_b()
        elif user_choice.upper() == "C":
            option_c()
        elif user_choice.upper() == "X":
            break
        else:
            print("Please choose one of the options")
    print("thank you for using the program")

def option_a():
    print("We're in option A here")

def option_b():
    print("We're in option B here")

def option_c():
    print("We're in option C here")

main()
