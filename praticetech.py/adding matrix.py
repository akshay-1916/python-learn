a=[[1,2,3],
   [3,5,4],
   [5,4,7]]

b=[[5,3,2],
   [3,2,4],
   [7,5,2]]

r=[[0,0,0],
   [0,0,0],
   [0,0,0]]


for i in range(len(a)):
    for j in range(len(b)):
        r[i][j]=a[i][j]+b[i][j]
        print(r[i][j],end="  ")
        
    print("")    
        
        