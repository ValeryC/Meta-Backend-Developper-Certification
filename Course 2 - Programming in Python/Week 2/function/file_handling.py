# This code demonstrates how to open a file in append mode and add new lines to it.

try:
    # Open the file 'text.txt' in append mode
    with open('text.txt', 'a') as file:
        # Write two new lines to the file
        file.writelines(["\nThis is a new line added to the file", "\nThis is another line added to the file"])
except FileNotFoundError as e:
    # If the file is not found, print an error message
    print("Error:", e)
    file.r