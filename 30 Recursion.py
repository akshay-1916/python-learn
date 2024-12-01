def fact(n):
    f=1
    i=1
    for i in range(1,n+1):
        f=f*i
    print(f)     
        
fact(4)        


def factorial(ff):
    if(ff==0 or ff==1):
        return 1
    
    else:
        return ff*factorial(ff-1)
    
print(factorial(5))    