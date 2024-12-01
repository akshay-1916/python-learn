class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showd(self):
        print(f"The Employee name is {self.name} and its id is {self.id}")
        
e=employee("akshay",15)
e.showd()          