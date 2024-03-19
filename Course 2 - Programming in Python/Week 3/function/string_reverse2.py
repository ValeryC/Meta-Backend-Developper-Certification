def string_reverse(str):
    reversed_str = "" # Create an empty string
    for char in str: # Loop through the string and check if the first and last characters are the same
        reversed_str = char + reversed_str # This will reverse the string
    return reversed_str # Return the reversed string

str = "reversal" # This will reverse the string "reversal" to "lasrever"
reverse = string_reverse(str) # Call the function and pass the string "reversal" as an argument
print(reverse) # lasrever