user_input = input("Enter your name: ")  # Prompt the user to enter their name
print("Your name is:", user_input)

num1 = input("Enter a number: ")  # Prompt the user to enter a number
num2 = input("Enter another number: ")  # Prompt the user to enter another number
print("the first number is:", num1)
print("the second number is:", num2)
print("the sum of the two numbers is:", int(num1) + int(num2))  # Calculate and print the sum of the two numbers

str1 = input("Enter your first name: ")  # Prompt the user to enter their first name
str2 = input("Enter your second name: ")  # Prompt the user to enter their second name
print("Your full name is:", str1 + " " + str2)
print("hello {} {}".format(str1, str2))