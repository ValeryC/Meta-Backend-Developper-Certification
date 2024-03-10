# Arithmetic Operators
x = 10 + 5  # Addition
y = 10 - 5  # Subtraction
z = 10 * 5  # Multiplication
w = 10 / 5  # Division
v = 10 % 3  # Modulo (Remainder)
u = 10 ** 2  # Exponentiation

# Comparison Operators
a = 10 == 5  # Equal to
b = 10 != 5  # Not equal to
c = 10 > 5  # Greater than
d = 10 < 5  # Less than
e = 10 >= 5  # Greater than or equal to
f = 10 <= 5  # Less than or equal to

# Assignment Operators
g = 10  # Assign value
g += 5  # Add and assign
g -= 5  # Subtract and assign
g *= 5  # Multiply and assign
g /= 5  # Divide and assign
g %= 3  # Modulo and assign
g **= 2  # Exponentiation and assign

# Logical Operators
h = True and False  # Logical AND
i = True or False  # Logical OR
j = not True  # Logical NOT

# Bitwise Operators
k = 10 & 5  # Bitwise AND
l = 10 | 5  # Bitwise OR
m = 10 ^ 5  # Bitwise XOR
n = ~10  # Bitwise NOT
o = 10 << 2  # Bitwise left shift
p = 10 >> 2  # Bitwise right shift

# Logical Operators (continued)
k = True and True  # Logical AND
l = True or False  # Logical OR
m = not False  # Logical NOT

# If statement example
if h and i:
    print("Both h and i are True")
elif h or i:
    print("Either h or i is True")
else:
    print("Neither h nor i is True")

# More logical operators example
a = True
b = True

k = a and b  # Logical AND

l = a or b  # Logical OR
m = not a  # Logical NOT
n = not b # Logical NOT

print("k =", k)
print("l =", l)
print("m =", m)

if m and n:
    print("all not true")

if a or not b:
    print("the condition pass.a is true b is not True")