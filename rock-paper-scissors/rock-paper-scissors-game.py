#################################################################################
# Name:                check_if_computer_wins
# Arguments:           computer_hand - R, P or S
#                      user_hand - R, P or S
# Return Value(s):     True/False - true if computer hand beats user hand
# Description:         Compare the two hands using the usual rules for R/P/S
#                      return true if the computer hand wins
#################################################################################
def check_if_computer_wins(computer_hand, user_hand):
    computer_wins = False
    if computer_hand == "R" and user_hand == "S":
        computer_wins = True
    elif computer_hand == "P" and user_hand == "R":
        computer_wins = True
    elif computer_hand == "S" and user_hand == "P":
        computer_wins = True
    return computer_wins