# It is technique for improving the performance of a program by storing the results of function call so that you can reuse the results instead of recomputing them every time the function is called.



from functools import lru_cache
from sys import maxsize
import time

@lru_cache(maxsize==None)
def f(n):
    time.sleep(n)
    return n*3
    
    
print(f(2)) 
print("after 4s")
print(f(3))
print("After 6s")  


print(f(2)) 
print("after 4s")
print(f(3))
print("After 6s")  