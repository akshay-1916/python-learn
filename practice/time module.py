import time

q=time.time()

i=0
for i in range(101):
     print(i)
    

e1=time.time()-q
print(e1)    
  
  

  
q=time.time()    
   
i=0    
while i<101:
    print(i)
    i=i+1    
    

e1=time.time()-q
print(e1)     


r=time.localtime()
w=time.strftime("%Y %m %d %H:%M:%S",r)
print(w)