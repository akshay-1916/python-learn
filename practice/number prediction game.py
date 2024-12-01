import random

a=random.randint(1,6)

q=input("Enter Player 1 Name:")
r=input("Enter Player 2 Name:")


print(f"Throw the Dice by {q}: {a}")

b=random.randint(1,6)
print(f"Throw the Dice by {r}: {b}")

if a==b:
    print("Tie")
elif a>b:
    print(f"{q} is Win")
    
else:
    print(f"{r} is Win")    
    
  