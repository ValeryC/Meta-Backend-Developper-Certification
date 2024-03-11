# # Functions and variables

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.Local scope
def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))
7
# Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 2. Enclosing scope
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    print(double)

    return total

# get_total(5, 2)
# # 14
# # error = NameError: name 'double' is not defined

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 3. Global scope

# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere. 
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total

print(get_total(3, 2))
