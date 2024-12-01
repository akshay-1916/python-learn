# It is special type of function that allow you to create an iterable sequence of value.This function return generator object,which can be use to generate the values one by one as you iterate over it. It give value one by one

def myge(): 
 for i in range(1000):
    yield i
    
g=myge()    
# print(next(g))
# print(next(g))
# print(next(g))

for j in g:
    print(j)