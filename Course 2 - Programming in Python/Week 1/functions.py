#len() length of word
length = len("hello")  # Calculates the length of the string "hello" and assigns it to the variable 'length'
print(length)  # Prints the value of 'length'

#str() convert to string
str(33)  # Converts the integer 33 to a string
print(type(str(33)))  # Prints the type of the result, which is <class 'str'>
print(str(33))  # Prints the string representation of 33

#int() convert to integer
int('75')  # Converts the string '75' to an integer
print(type(int('75')))  # Prints the type of the result, which is <class 'int'>
print(int('75'))  # Prints the integer representation of '75'

#float() convert to float
some_int = 10  # Assigns the integer 10 to the variable 'some_int'
print(type(float(some_int)))  # Converts 'some_int' to a float and prints its type, which is <class 'float'>
print(float(some_int))  # Converts 'some_int' to a float and prints the result

print('defining a function')
# def defining a function
def add(a, b):  # Defines a function 'add' that takes two arguments 'a' and 'b'
    return a + b  # Returns the sum of 'a' and 'b'
value = add(3, 4)  # Calls the function 'add' with arguments 3 and 4, and assigns the result to 'value'
print(value)  # Prints the value of 'value'