# When a class drive from anather class.The child class will inherit all the public and protected properies and methods from the parent class
# It have 5 types

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showd(self):
        print(f"The Employee name is {self.name} and its id is {self.id}")
        
class s(employee):
    def showlanguage(self):
            print("The default language is python")
        
e=employee("akshay",15)
e.showd()    

q=s("harry",20)
q.showd()
q.showlanguage()      