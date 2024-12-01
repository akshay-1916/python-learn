a={
    33:"akshay",
    39:"kokare",
    66:"man",
    44:"boy"
}

# print(a[44])
# print(a.get("akshay"))
# print(a.values())
# print(a.keys)


for key in a.keys():
    print(f"The value corresponding to the key {key} is {a[key]}")
    
print(a.items())