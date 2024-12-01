# I work parallaly
import threading
import time


def func(sec):      #function
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    
t=time.perf_counter()
# normal code    
# func(3)    
# func(2)
# func(4)

# same code using threads
t1=threading.Thread(target=func,args=[2])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()
tt=time.perf_counter()
print(tt-t)
