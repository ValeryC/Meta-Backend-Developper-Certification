def square(num):
    return num * 2

print(square(5)) # 10

# map() function
data = [2,3,5,7,11,13,17,19,23,29,31]
newdata = map(square, data) # map() function returns a map object
print(list(newdata)) # [4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62]
newdata = [x + 3 for x in data]
print(newdata) # [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]