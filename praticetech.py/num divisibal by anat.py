# using loop
num=int (input("Enter a number:"))
up=int(input("Enter the upper limit:"))
for i in range(up+1):
   if i%num==0:
       print(i)
       
# using lambda    

l=[39,48,23,6,65,87,22]

result=list(filter(lambda x:x%num==0,l))