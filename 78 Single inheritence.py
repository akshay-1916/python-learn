# It is type of inheritance properties and behaviors from a single parent class .It is simplest and most common from of inheritance


class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def makes(self):
        print("Sound made by the animal")
        
class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="a")
        self.breed=breed
        
    def makes(self):
        print("bark!")    
        
d=dog("D","o") 
d.makes()  

a=animal("dog",77)          
a.makes()     
                  