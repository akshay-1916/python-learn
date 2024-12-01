num=int (input("Enter the number:"))

if num<0:
    print("please Enter positive number")
    
else:
    s=0
    while num>0:
        s=num+s
        num=num-1
    print(s)            