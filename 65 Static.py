# Static method in Python are Methods that belong to class rater than an instance of class.They are define using the @staticmethod decorator and do not have access to the instance of the class(i.e.self).
# They are called on the class itself,not on an instance of the class

class a:
    def __init__(sedlf,num):
        sedlf.num=num
        
    def addnum(sedlf,n):
        sedlf.num=sedlf.num+n
        print(sedlf.num)
        
    @staticmethod
    def add(a,b):
        return a+b
    
        
        
e=a(3)
e.addnum(5)

print(a.add(10,10))            
