a=4
b="4"

print(a is b) #exact location of object in memory
print(a==b) #value

d=[2,3,56]
f=[2,3,56]

print(d is f)
print(d == f)

r={4,6}
t={4,6}
print(r is t)
print(r == t)


e=None
q=None

print(e is q)
print(e == q)


