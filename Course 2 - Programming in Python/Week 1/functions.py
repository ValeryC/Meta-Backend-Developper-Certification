#len() length of word
length = len("hello")
print(length)

#str() convert to string
str(33)
print(type(str(33)))
print(str(33))

#int() convert to integer
int('75')
print(type(int('75')))
print(int('75'))

#float() convert to float
some_int = 10
print(type(float(some_int)))
print(float(some_int))

print('defining a function')
# def defining a function
def add(a, b):
    return a + b
value = add(3, 4)
print(value)