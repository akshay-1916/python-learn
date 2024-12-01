
def fun1():
  try:
    l=[1,2,3,4,5]
    i=int(input("Enter a number:"))
    print(l[i])
    # return 1
  except:
    print("Some error occured")
    # return 0
    
  finally:
    print("I am always execute.")    
    
x=fun1()
print(x)    