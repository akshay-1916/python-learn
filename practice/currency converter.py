print("************Currency Converter*********** ")
w="yes"
n=input("You want Try it :")

while(w==n.lower()):
 
 c=int(input("Enter the Currency in Indian Rupee:"))
 print("Select The Currency in which you want Convert")
 ch=int(input("1.Doller \n2.Shri Lanka Rupee \n3.Euro \n4.Canadian Doller \n5.Australia Doller\n"))
 
 match ch:
    case 1:
      print("In Doller:",c*(12*0.001))
     
    case 2:
      print("In Sri Lanka Rupee:",c*(3.56))
    case 3:
      print("In Euro:",c*(0.011))
      
    case 4:
      print("In Canadian Doller:",c*(0.016))
    
    case 5:
        print("In Australian Doller:",c*(0.018))
        
    case _:
        print("Enter VAlid Choice")    
        
            
print("Thank you")        
       



