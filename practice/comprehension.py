# num=int(input("Enter a number : "))

# n=[i*num for i in range(1,11)]

# print(n)

def comp(filename):
    num=int(input("Enter a number : "))

    n=[i*num for i in range(1,11)]

    # print(n)
    with open(filename,'a') as f:
        f.write(str(n))
        f.write("\n")

comp("text/comp.txt")

with open("text/comp.txt",'r') as f:
    print(f.read())