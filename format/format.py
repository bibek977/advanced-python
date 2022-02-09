name = "bibek"
surname = "bhattarai"
age = 25

get1= f"hello, {name} {surname} : {age}"
print(get1)

get2= "hello, {} {} : {}".format(name,surname,age)
print(get2)

get3= "hello, {1} {0} : {2}".format(name,surname,age)
print(get3)