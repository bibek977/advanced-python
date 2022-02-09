numbers = [2,45,67,43,446,432,26,64,56,77,734]

num=[]

for item in numbers:
    if item%2 ==0:
        num.append(item)

print(numbers)
print(num)

n=[i for i in numbers if i%2!=0]
print(n)