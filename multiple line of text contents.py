# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Set the filename to "mylife.txt"
file_name = "mylife.txt"
# Using the with statement, open the file in write mode.
with open(file_name, "w") as f:
    # Ask the user to input their first name.
    first_name = input("Enter your first name: ")
    # Loop until the user commands there are no more lines to enter
    while True:
        # Ask the user to enter a line
        line = input("Enter line: ")
        # Using the write() method, add the line to the file followed by a newline character.
        file_name.write(line + "\n")
# Ask the user if there are more lines to enter.
# Exit the loop if the user enters "n"
# Ask for another line to enter if the user enters "y".
# Ask again if the user enters anything else.