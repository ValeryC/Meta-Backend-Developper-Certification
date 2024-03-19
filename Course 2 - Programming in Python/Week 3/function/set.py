set_a = {x for x in range(10,20) if x not in [12,14,16]} # set comprehension with if condition  
print(set_a) # {10, 11, 13, 15, 17, 18, 19}

# Sets and lists are both data structures in Python, but they have some key differences:
# Ordering: Lists maintain the order of elements, meaning that the elements are stored in a 
# specific sequence. Sets, on the other hand, do not preserve the order of elements. 
# The elements in a set are unordered.

# Duplicates: Lists allow duplicate elements, which means you can have multiple occurrences 
# of the same value in a list. Sets, on the other hand, do not allow duplicates. 
# If you try to add a duplicate element to a set, it will be ignored.

def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i # return_value = return_value * i
    return return_value

factorial(4)

