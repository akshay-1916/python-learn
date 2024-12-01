# append==push

class lab:
    def __init__(self):
        self.books=[]
        self.nubook=0
        
        
    def addbook(self,book):
       self.books.append(book)
       self.nubook=len(self.books)
       
    def show(self):
        print(f"The library has {self.nubook} books")   
       


f=lab()
f.addbook("akshay")
f.addbook("aks")
f.show()

