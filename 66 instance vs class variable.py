class akshay:
    cn="Apple"        #class variable
    nemployee=0
    
    
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll     #instance variable
        self.amo=19
        akshay.nemployee +=1
        
    def show(self):
        print(f"Name is {self.name} and it Roll number is {self.roll} and and Its amount is {self.amo} Its company is {self.cn} and Number of employee is{self.nemployee}")
        
        
a=akshay("ak",15)
a.cn="microsoft"
a.show()   
print("\n")
b=akshay("kok",200)
b.show()          