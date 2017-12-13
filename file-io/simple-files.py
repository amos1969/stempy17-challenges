######################################################################################################
# simple-files.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: Simple File Handling
#
# Examples of simple file handling
#######################################################################################################

# How to write data to a file

# Open (or create) a file which we are going to append to (that's what the a is for, use w to overwrite)
file_handle = open("some_text_file.py", "a")

# This will write the text to the file with a new line at the end of the line
file_handle.write("We're going to write this line of text to a file, called some_text_file.txt\n")


# When we finish using the file, we have to close the file_handle so that we don't use up all
# the system resources
file_handle.close()





