# constructor is use to initalize the value,it allow you to create and initialize object of given class.
# It always return none
# It call when Object call
# Types:Parameterized,default
# self represent the instance of class. By using the "self" we can access the attributes of and methods of the class in python.


class person:
    def __init__(self,name,occ):
        print("Hay I am a person")
        self.name=name
        self.occ=occ
    
    def inf(self):
        print(f"{self.name} is a {self.occ}")
        
        
a=person("Harry","man")
a.inf()        