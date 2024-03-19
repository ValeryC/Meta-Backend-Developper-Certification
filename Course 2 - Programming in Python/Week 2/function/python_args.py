# Description: This file demonstrates the use of *args in Python
# This function takes any number of arguments and returns their sum.
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of( 3, 9, 10, 123, 21, 123, 123)) # 412