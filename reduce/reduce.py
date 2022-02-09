from functools import reduce

l=[1,2,3,4,5]

sum = lambda a,b : a+b

mul = lambda a,b : a*b

# l1=reduce(sum, l, 0)
l1=reduce(sum, l)
print(l1)

# l2=reduce(mul, l, 1)
l2=reduce(mul, l)
print(l2)