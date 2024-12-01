# 153=cube(1)+cube(5)+cube(3)=


n=int(input("Enter the number:"))
t=n
s=0
digit=len(str(n))
while t>0:
    d=t%10
    c=d**digit
    s=s+c
    t=t//10




if s==n:
    print(f"{n} is Armstrong number")
    
else:
    print(f"{n} is not Armstrong number")   