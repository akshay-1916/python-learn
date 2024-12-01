print("Welcome to Quiz Game")

ans=input("Are you want Play Game (Yes/No): ")
s=0
if ans.lower()=="yes":
    ans=input("What is your name:")
    if ans.lower()=="akshay":
        print("Correct")
        s=s+1
    else:
        print("Wrong")    
        
    ans=input("How Old are You:")
    if ans.lower()=="19":
        print("Correct") 
        s=s+1
    else :
        print("Wrong")       
     
    print("Thankyou for Playing this Game")
    print(f"Your Score is {s}")
        
if ans.lower()=="no":
    print("Stop")        