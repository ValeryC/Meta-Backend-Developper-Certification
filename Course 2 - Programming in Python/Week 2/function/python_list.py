from os import sep
list1 = [1,2,3,4,5]

list2 = ['A','B','C']

list3 = ['Hello', 1, True, 40.22]

list4 = [1, [2,3,4], 5, 6]

# This operator is used to unpack the elements of the list "*".
#In this case, *list1 will unpack the elements of list1, and print(*list1) will print the elements of list1 separated by spaces.
print(*list1) # 1 2 3 4 5

# The sep parameter is used to separate the elements of the list.
print(list1, sep = " ") # [1, 2, 3, 4, 5]

# The append() method adds an element to the end of the list.
list1.append(6)
print(list1) # [1, 2, 3, 4, 5, 6]

# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
list2.extend(['D','E','F'])
print(list2) # ['A', 'B', 'C', 'D', 'E', 'F']
print(list1.pop(4)) # 5
print(list1) # [1, 2, 3, 4, 6]

# The insert() method adds an element to the list at a given index.
list3.insert(3, 'World')
print(list3) # ['Hello', 1, True, 'World', 40.22]
