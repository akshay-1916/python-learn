import time
def forl():
    i=0
    for i in range(100):
        print(i)
        
        
def whilel():
    i=0
    while i<100:
        print(i)
        i=i+1
                
                
q=time.time()                
forl()
t1=time.time()-q
print(t1)
r=time.time()
whilel()  
t2=time.time()-r
print(t2)   
           
           
print(4)
time.sleep(5)
print("This is printed after 5 second")


g=time.localtime()
ss=time.strftime("%Y-%m-%d %H:%M:%S",g)
print(ss)
           