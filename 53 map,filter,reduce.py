# def cube(x):
#     return x*x*x

# l=[1,2,3,4,5,6]
# cl=list(map(cube,l))
# print(cl)


sum=lambda x:x*x*x

l=[1,2,3,4,5,6]
# map
sl=list(map(sum,l))
print(sl)

# filter
def filter_fu(a):
    return a!=2

newnewl=list(filter(filter_fu,l))
print(newnewl)


# reduce
from functools import reduce

num=[1,2,3,4,5,6]
sum=reduce(lambda x,y:x+y,num)

print(sum)
