import random

n=random.randint(1,20)
print(n)
c=1
a=0
print("Player 1")
while(n!=a):
   a=int(input("Predict the Number(1-20):"))

   if(n>a):
       print("Predict Greater Number:")
       c=c+1
       
   if(n<a):
       print("Predict Lower Number")    
       c=c+1
       
print(f"You guess number {n} in {c} attempts")       

print("\n")

n=random.randint(1,20)
r=1
b=0
print("Player 2")
while(n!=b):
   b=int(input("Predict the Number(1-20):"))

   if(n>b):
       print("Predict Greater Number:")
       r=r+1
       
   if(n<b):
       print("Predict Lower Number")    
       r=r+1
       
print(f"You guess number {n} in {r} attempts")     
  
print("\n")
    
if(r>c):
    print("Player 1 is Win")
    
if(r<c):
    print("Player 2 is Win")    