def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1) # recursive call

a = sum(5) # 5 + 4 + 3 + 2 + 1 + 0
print(a) # 14

# 5 + sum(4)
# 5 + 4 + sum(3)
# 5 + 4 + 3 + sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 0 = 14


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)