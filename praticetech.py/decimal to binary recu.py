def cb(n):
    if n>1:
        cb(n//2)
    print(n%2,end="")
    
cb(15)         