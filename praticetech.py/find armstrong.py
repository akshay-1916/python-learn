lower=int(input("Enter the lower Number:"))
upper=int(input("Enter the upper Number:"))


for num in (lower,upper+1):
    order=len(str(num))
    t=num
    s=0
    digit=len(str(num))
    while t>0:
       d=t%10
       c=d**digit
       s=s+c
       t=t//10

        
    if num==s:
           print(num)
        
            
    