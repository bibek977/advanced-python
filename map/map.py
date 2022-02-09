def square(num):
    return num*num
    
def cube(num):
    return num*num*num

l1=[1,2,3,4]

l2=[]
for i in l1:
    l2.append(square(i))
print(l2)

l3=list(map(cube, l1))
print(l3)