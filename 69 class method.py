# class method is type of method that is bound to the class and not the instance of the class.

class aks:  
    comp="akshay's company"
    
    def a(skkk):
        print(f"The name is {skkk.name} and Company is {skkk.comp}")
        
    def changec(self,compnew):
        self.comp=compnew
        
        
q=aks()
q.name="kokare"
q.a()  
q.name="alex"      
q.changec("akkk's company")
q.a()
            