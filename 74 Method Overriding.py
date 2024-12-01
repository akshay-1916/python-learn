# It is powerfull future that allow you to redefine a method in a derived class.


class a:
    def __init__(self,c,b):
        self.c=c
        self.b=b
        
    def area(self):
        return self.b*self.c
    
class circle(a):
    def __init__(self,redius):
        self.redius=redius
        super().__init__(redius,redius)
        
    def area(self):
        return 3.14*self.redius*self.redius
    
            
rec=circle(3)
print(rec.area())  
            