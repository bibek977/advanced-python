def Inc(num):
    try:
        # print(num + 1)
        return int(num) + 2

    except:
        raise ValueError("This is Custom Error")
        # print(Error1)

print(Inc(5))
# print(Inc("sd"))