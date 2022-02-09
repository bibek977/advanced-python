import random
print("From 0 -9")
rand= random.randint(0,10)

while(True):
    print("Type q or Q to quit")
    num = input("Enter a number : ")
    if(num=='q' or num=='Q'):
        break
    try:
        n=int(num)
        if(n==rand):
            print("Right Guess")
            break
        elif(n<rand):
            print("Guess Higher")
        elif(n>rand):
            print("Guess Lower")

    except Exception as b:
        # print(f"Error : {b}")
        print(f"Error : {b.__str__()[20::]}")

print("Thanks")

