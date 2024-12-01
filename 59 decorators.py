# function which change other function and return It

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks")
        return mfx
@greet
def hello():
    print("Hello Word")
    
@greet
def add(a,b):
    print(a+b)
    
hello()

add(1,3)    