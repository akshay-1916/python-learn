class E:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @classmethod
    def fromstr(cls,str):
        return cls(str.split("-")[0]),
int(str.split("-")[1])    
        
e=E("akshay",60000)
print(e.name)
print(e.salary)

str="ak-111111"
e2=E.fromstr(str)
print(e2.name)

        