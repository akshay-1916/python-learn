sum=0

while(True):
    n=input("Enter a price:")
    if n!="q":
        sum=sum+int(n)
        print(f"Order total so far: {sum}")
        
    else:
        print(f"Your Bill is :{sum}")
        break    
        
    