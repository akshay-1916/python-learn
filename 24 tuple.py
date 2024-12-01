# we can't change tuple
tup=(1,3,4,77,"ak",True)

print(tup)
print(type(tup),tup)
if 4 in tup:
    print("yes")
    
tup2=tup[:5]    
print(tup2)
print(tup[2:])
print(tup[3])