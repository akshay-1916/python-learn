print("Welcome to KBC")

print("Q1.which colore is dark?")
print("A.Green\nB.black\nC.yellow\nD.pink\n")
c=0
a=int(input("Enter your Choice:"))
print(a)
if(a<2 and a>0):
    print("Correct")
    c=c+1000
else:
    print("Wrong")    

print("your score is:",c)