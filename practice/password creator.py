import random

a=random.random()
print(a)

b=a*123

c=int(input("Enter your Password:"))
p=(c*b)
print("Your Secrate code is ",p/123)


v=input("You want See your Password (yes/no):")
  
if v.lower()=="yes":
    print(f"Your password is {c}")
    
else:
    print("Okay")    