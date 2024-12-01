# Access Specifier /MOdifiers
# It use to limit the access of class variables and class methods outside of class while implimenting the concepts of inheritance.

# Type:Public:all variable and method are default public ,__Private,_Protected

class Employee:
    def __init__(self):
        self.__name="akshay"
        
        
a=Employee()
# print(a.__name)  #Cannot be accessed direction
print(a._Employee__name)  #Cannot be Accessed indirectly

print(a.__dir__())