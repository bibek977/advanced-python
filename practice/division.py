try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))

    print(a/b)

except ZeroDivisionError:
    print("infinite")

finally:
    print("done")