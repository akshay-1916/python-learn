# It the double underscores surrounding their name,are power tools that allow you to customize the behaviour of your classes.

# __init__ method:It is special method that is automatically invoked when you creat a new instance of class. This method is responsible for setting up the object's initial state ,and it is where you would typically defin any instance variable that you need.
# Also called constructor


class Employee:
    def __init__(self,name):
        self.name=name
        
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return i
        
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    def __repr__(self):
        return f"Employee ('{self.name}')"
    
    def __call__(self):
        print("Hay I am good")   
        
e=Employee("akshay")  
print(e.name)            
print(len(e))
print(str(e))
print(repr(e)) 
e()  #call

# The str and repr method both are use to convert an object to a string representation. The str method is use when you want to print out an object,while the repr method is used when you want to get a string representation of an object that can we use to recreate a object.  