######################################################################################################
# more-complex-files.py by Dave Ames
# david.john.ames@gmail.com
# @davidames
#
# Problem: More Advanced File Handling
#
# Examples of more advanced file handling
#######################################################################################################
# Create an empty list
the_text = []
# Open the file for reading, and assign it to the variable file_handle
file_handle = open("pi-poems.txt", "r")

# Loop through the file, reading one line at a time into the line variable
for line in file_handle:
    # Removes non-printing characters like newlines
    line = line.strip()
    # Add the current line to the end of the list we created
    the_text.append(line)

# Close the file
file_handle.close()

# Pull each item out of the list, one at a time
for item in the_text:
    # Print each item on a single line
    print(item)