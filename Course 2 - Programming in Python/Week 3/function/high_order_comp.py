def hof_add(increment):
    # Create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + increment)
        return new_numbers
    # We return the function as we do any other value
    return add_increment

add5 = hof_add(5) # add5 is a function that adds 5 to the numbers in the list passed to it.
print(add5([23, 88]))   # [28, 93] # [23+5, 88+5]
add10 = hof_add(10)
print(add10([23, 88]))  # [33, 98] # [23+10, 88+10]

# The map function is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping.
names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)

# This prints something similar to: <map object at 0x10ed93cc0>
print(greeted_names)
# Recall, that map returns an iterator 

# We can print all names in a for loop
for name in greeted_names:
    print(name)

# The filter function is a built-in function that allows you to process and filter all the items in an iterable using a function that you provide.
arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21))) 
# map and filter can be combined to process and filter the items in an iterable using a function that you provide.
# This prints something similar to: <map object at 0x10ed93cc0>

print(list(arbitrary_numbers)) # [27, 216, 729, 1728, 3375, 5832]