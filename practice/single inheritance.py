class cat:
    def __init__(self,name,spe):
        self.name=name
        self.spe=spe
        
    def m(self,sound):
        self.sound=sound
        print(f"Hi {self.name}"  )  
    
class c(cat):
    def __init__(self):
        cat.__init__(self,name="tomy")
        
    def ms(self):
        print("mauuu")
        
q=cat("cat",2)
q.m("mau")               