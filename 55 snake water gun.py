import random

c=["snake","water","gun"]

a=random.choice(c)
print(a)


p=input("Enter Your Choice \nSnake \tWater \tGun\n:::")

if a==p.lower():
    print("tie")
    
    
if a==p.lower():    
 if a=="snake" and p.lower()=="water":
    print("You Lost")   
    
 if a=="water" and p.lower()=="gun":
    print("You Lost")       


 if a=="gun" and p.lower()=="snake":
    print("You Lost")
    
else:
    print("You Win")        