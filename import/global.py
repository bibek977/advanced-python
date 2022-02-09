a=5
def show():
    global a
    print(a)
    a=10
    print(a)

show()
print(a)