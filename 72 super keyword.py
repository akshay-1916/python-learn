# super() keyword in python is used to refer to the parent class .It is especially useful when class inherit multiple class parent classes and you want to call a method from one of parent classes.



class pro:    #super class
   def __init__(self,name,salary):
       self.name=name
       self.salary=salary
       
class programer(pro):   #sub class 
    def __init__(self,name,salary,id):
        super().__init__(name,salary)
        self.id=id  
        
ak=programer("akshay",15,1200)      
print(ak.name) 
print(ak.id)      
print(ak.salary)