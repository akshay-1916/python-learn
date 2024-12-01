# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.Exception handling deals with these events to avoid the program or system crashing,and without this process,exception would disrupt the normal operation of a program.


# a=input("enter a number:")
# print(f"Table of {a}")
# try:
#  for i in range(1,11):
#     print(f"{a} X {i}={int(a)*i}")
    
# except Exception as e:
#     print("sorry some error occure")    

try:
    num=int (input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")    
    
except IndexError:
    print("Index Error")    