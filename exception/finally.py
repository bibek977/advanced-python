num=input("Enter a number : ")
try:
    num=int(num)
    print(num)

except:
    print("Error")
    exit()

finally:
    print("finally done")