name=["bibek","john","mary","cathrine"]

# n=[i for z,i in enumerate(name) if z%2==0]

n=[i for z,i in enumerate(name) if z==0 or z==2]

print(n)