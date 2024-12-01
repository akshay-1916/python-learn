import random

options=["Rock","Paper","Scissors"]

cc=random.choice(options)
uc=input("Rock/Paper/Scissors :")
print("Game: Rock / Paper /Scissors")
print("You VS Computer")
print("Your Chose :",uc)

print("Computer Chose :",cc)

if uc.capitalize()==cc:
    print("It's a tie")
    
    
elif  uc.capitalize()=="Rock" and cc=="Scissors":
    print("You Win")
      
      
elif  uc.capitalize()=="Paper" and cc=="Rock":
    print("You Win")      
      
elif  uc.capitalize()=="Scissors" and cc=="Paper":
    print("You Win")

else:
    print("Computer Win")
    
    