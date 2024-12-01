# It is new addition to python 3.8 and allows to you to assign a value to a variable within an expression.This can de useful when you need to use a value multiple times in loop, but don't want to repet the calculation.
#  this oprator represent := syntax



a=True
print(a)
print(a:=False)

num=[1,2,3,4,5]
while (n:=len(num))>0:
    
    print(num.pop())
    
# foods=list()
# while True:
#     food=input("enter the food:")
#     if food=="quit":
#         break
#     foods.append(food)    
    
foods=list()
while (food:=input("Enter the food:")) !="quit":
    foods.append(food)    