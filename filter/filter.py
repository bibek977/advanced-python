l = [12,45,56,76,83,99]

def greater(n):
    if(n>50):
        return True
    else:
        return False

lesser = lambda n : n < 50

l2=list(filter(greater, l))
print(l2)

l3=list(filter(lesser, l))
print(l3)