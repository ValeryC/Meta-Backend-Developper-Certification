set_k = {1,1,2,3,4,5,5} 
print(set_k) # {1, 2, 3, 4, 5} => duplicate values are removed 
set_a = {1, 2, 3, 4, 5, 6, 7}
set_b  = {6, 7, 8, 9, 10}
set_a.remove(3) # remove 3 from the set
print('set_a =',set_a) # {1, 2, 4, 5}


# The union() method returns a new set with all items from both sets:
set_c = set_a.union(set_b)
print('set_c =',set_c) # {1, 2, 4, 5, 6, 7, 8, 9, 10}
print('set_a | set_b =',set_a | set_b) # {1, 2, 4, 5, 6, 7, 8, 9, 10}

# The intersection() method returns a new set with items that are common to both sets:
set_d = set_a.intersection(set_b)
print('set_d =',set_d) # {6, 7}
# Another way to get the intersection of two sets is to use the & operator:
print('set_a & set_b =',set_a & set_b) # {6, 7}

# The difference() method returns a set that contains the difference between two sets.
set_e = set_a.difference(set_b) 
print('set_e =',set_e) # {1, 2, 4, 5}

# ^ operator returns a set that contains all items from both sets, except items that are present in both sets:
print(set_a ^ set_b) # {1, 2, 4, 5, 8, 9, 10} so {6 7} are removed from the set



