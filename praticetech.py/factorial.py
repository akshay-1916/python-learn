f=1
n=int(input("Enter a number:"))

for i in range(1,n+1):
    if n==0 or n==1:
        print("factorial is 1")
        
    else:
        f=f*i    
print(f)


import math

print(math.factorial(7))