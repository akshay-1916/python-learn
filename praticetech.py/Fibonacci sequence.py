# concept:continious adding of first two number

a=0
b=1
fb=1
n=int (input("How  many fibonacci number:"))

for i in range(1,n+1):
    fb=a+b
    a=b
    b=fb
    # fb=a+b
    print(fb)
