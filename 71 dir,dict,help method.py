a=[123,34,55]
print(dir(a)) #dir show methodss which we perform on that
# the dir() method, this function return a list of all the attributes and methods(include dunder method) available for an object.It is a useful tool for discovering what you can do with an object. 
print(a.__add__)


class person :
    def __init__(self,name,age):
        self.name=name  #attributes
        self.age=age
        
#The __dict__ attribute returns a dictionary represention of an object's attributes.It is a useful tool for introspection 
p=person("John",30)
print(p.__dict__)  

print(help(person))  
#The help() function is used to get help documentation for an object ,including a description of its attributes and methods. 

      