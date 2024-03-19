# Description: Python script to demonstrate the use of **kwargs in Python
# **kwargs is used to pass a keyworded, variable-length argument list
#  to a function. You should use **kwargs if you want to handle named arguments in a function.
# This function takes any number of keyword arguments and returns their sum.
def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2) # round to 2 decimal places

print(sum_of(a = 3, b = 9, c = 10, d = 123, e = 21, f = 123, g = 123)) # 412
