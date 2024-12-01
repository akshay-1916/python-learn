print("CALCULATER")
b=int(input("Enter First value:"))
c=int(input("Enter Second value:"))


a=int(input("Enter the number betwin 1 and 5 :\n1.Addiiton \n2.Substraction\n3.Multiplication \n4.Dividetion\n5.Modulus\n"))



match a:
    case 1:
        print("Addition is ",(b+c))
        
    case 2:
        print("Substraction is ",(b-c)) 
        
    case 3:
        print("Multiplication is ",(b*c))    
        
    case 4:
        print("Division is ",(b/c))  
        
    case 5:
        print("Modulas  is ",(b%c))       
        
    case _:
        print("Envalid input")       
        
        
        