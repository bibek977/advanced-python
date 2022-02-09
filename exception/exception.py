try:
    num=int(input("Enter a number : "))
    n=1/num
    print(n)

except ZeroDivisionError as z:
    print("Zero division Error")
    print(z)
    print(type(z))

except ValueError as v:
    print("Value Error")
    print(v)
    print(type(v))

except Exception as e:
    print("Exception Error")
    print(e)
    print(type(e))

print("Thanks")