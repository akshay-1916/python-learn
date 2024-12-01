# It is a future in python that allows developer to redefine the behavior of mathematicel and comparison operators for custom data type.
# That means that you can use standard mathamatical operators (+,-,/,*,etc) and comparison operators(>,<,==,etc) in your own classes.

 
class vector:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
 
    def __repr__(self):   #or __str__
        return f"{self.a}i +{self.b}j+ {self.c}k"
    
    def __add__(self,x):
        return vector(self.a+x.a,self.b+x.b,self.c+x.c)  
    
    def __mul__(self,x):  #__sub__ ,__pow__,etc.
        return vector(self.a*x.a,self.b*x.b,self.c*x.c)
    
   
    
v1=vector(2,3,4)
print(v1)          
 
        
v2=vector(5,3,1)
print(v2) 

print(v1+v2)   
print(type(v1+v2))  
print(v1*v2)
