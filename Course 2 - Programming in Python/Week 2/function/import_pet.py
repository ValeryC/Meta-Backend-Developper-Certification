# Description: This script will import the petnames.txt file
# and print a random pet name from the file.

import random # Import the random module
f = open("petnames.txt", "r") # Open the file and read the content
f_content = f.read() # Read the content of the file
f_content_list = f_content.split("\n") # Split the content of the file by new line
f.close() # Close the file
print(random.choice(f_content_list)) # Print a random pet name from the file