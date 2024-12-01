# multiple parent class in one child class

class pen:  #parent class
    def __init__(self,name):
        self.name=name
        
class notebook:   #parent class
    def __init__(self,nb):
        self.nb=nb
        
        
class all(pen,notebook):   #child class
    def __init__(self,name,nb):
        self.name=name                
        self.nb=nb
        
        
e=all("Selogriper","sundaram")            
print(e.name)
print(e.nb)        
print(all.mro())