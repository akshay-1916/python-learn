# like switch

a=int(input("enter a number from 1 to 5:"))

match a:
    case 1:print("you give 1")
    
    case 2:print("you give 2")
    
    case 3:print("you give 3")
    
    case 4:print("you give 4")
    
    case 5:print("you give 5")
    
    case _ if a!=3:print("you not choose 3")
    
    case _:print("enter a number between 1 to 5")
    
    