# Algorithe: Palindrome Checker
def is_palindrome(str):
    startIndex = 0
    endIndex = len(str) - 1 

# Loop through the string and check if the first and last characters are the same
    for x in str:
        if str[startIndex] != str[endIndex]: # If the first and last characters are not the same, return False
            return False
        return True # If the first and last characters are the same, return True
    
print(is_palindrome("madam")) # True
print(is_palindrome("racecarwee")) # False
    

