# Tuple can mix different data types and are immutable
# explain immutable => cannot be changed after creation
my_tuple = (1, 'string', 3.14, True)  # Tuple can be declare with or without parenthesis
print(my_tuple) # (1, 'string', 3.14, True)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple.index(3.14)) # 2

for x in my_tuple:
    print(x) # 1 string 3.14 True => each on a new line 

my_tuple[0]= 2 # TypeError: 'tuple' object does not support item assignment