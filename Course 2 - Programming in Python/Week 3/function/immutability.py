mutable_collection = ['Tim', 10, [4, 5]] # list
immutable_collection = ('Tim', 10, [4, 5]) # tuple

# Reading from data types are essentially the same:
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5]

# Let's change the 2nd value from 10 to 15
mutable_collection[1] = 15

# This fails with the tuple
immutable_collection[1] = 15