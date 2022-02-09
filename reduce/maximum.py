from functools import reduce

num = [4,6,2,9,5]

# def max(n,m):
#     if(m>n):
#         return m
#     else:
#         return n

# max = lambda m,n : m if (m>n) else n

output = reduce(max, num)
print(output)

output = reduce(min, num)
print(output)