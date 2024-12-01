# It is method that use to access the values of an object's properties.
# It use to return specific property.

class Myclass:
    def __init__(self,value):
        self._value=value
        
        
    def show(self):
        print(f"Value is {self._value}")
    #  getattr    
    @property
    def ten(self):
        return 10*self._value
    
    # setter
    @ten.setter
    def ten(self,new_value):
        self._value=new_value/10
    
obj=Myclass(10)

print(obj.ten)            
obj.show()