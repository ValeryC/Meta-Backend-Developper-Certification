list = [1, 2, 3]
# not a pure function
# cause it modifies the original list
# def add_to_list(lst, value):
#     lst.append(value)
#     return lst

# result = add_to_list(list, 4)
# print(result)


# pure function
# does not modify the original list
def add_to_list(lst, value):
    nl = lst.copy() # create a new list and copy the original list into it
    nl.append(value) # append the value to the new list
    return nl # return the new list

new_list = add_to_list(list, 4)

print(new_list) # [1, 2, 3, 4] new list is modified
print(list) # [1, 2, 3] original list is not modified
