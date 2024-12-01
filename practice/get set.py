class m:
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print(f"Value is {self._value}")
        
    # getter  
    @property  
    def ten(self):
        return 10*self._value
    
    # setter
    @ten.setter
    def ten(self,newvalue):
        self.value=newvalue/10 
        
obj=m(9)
print(obj.ten) 
obj.show()      
    