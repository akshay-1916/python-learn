class a:
    def ak(self,name):
        self.name=name
        print (f"{self.name}")
class b(a):
    def aksh(self,name):
        self.name=name
        print (f"{self.name}")

class c(b):
   def akshay(self,n):
        self.n=n
        print (f"{self.n}")
q=a()
q.ak("kok")  

w=c()
print(w.ak("qwweer")) 
