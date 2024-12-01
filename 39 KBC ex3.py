questions=[
    ["Q.what is greatest 3 digit number?","222","444","555","999","none",4],
    ["Q.Which is 1 digit greatest number?","1","3","5","9","none",4],
    ["Q.what is greatest 4 digit number?","222","4449","555","999","none",2],

    ["Q.what is greatest 3 digit number?","2292","444","555","999","none",1]

]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,0]
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for rupees {levels[i]}")
    print(f"{question[0]}")
    print(f"A. {question[1]}    B.{question[2]}")
    print(f"C. {question[3]}    D.{question[4]}")
    
    reply=int(input("Enter your answer (1-4) or 0 to Quit :"))
    if (reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer,you have R.{levels[i]}")
        if i==4:
           money=10000
        elif i==9:
            money=320000
            
        elif i==12:
            money=10000000     
        
        
    else:
        print("Wrong answer")
        break
    
print(f"You total win {levels[i-1]}")        