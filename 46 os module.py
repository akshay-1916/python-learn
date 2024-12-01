print("Welcome to code and Decode")
d=int(input(print("1.code \n2.Decode")))
if(d==1):
    nword=[]
    st=input("enter a statement:")
    r1="asf"
    r2="rio"
    r3="rfh"
    r4="efi"
    stnew=r1+st[1:]+st[0]+r2
    stnew=r4+stnew+r3
    
    nword.append(stnew)
    
    print(" ".join(nword))
if(d==2):
    nword=[]
    st=input("enter a statement:")
    r1="asf"
    r2="rio"
    r3="rfh"
    r4="efihf"
    stnew=st[3:-3]
    stnew=stnew[3:-3]
    stnew=stnew[9:]

    # stnew=st[]
    
    nword.append(stnew)

    print(" ".join(nword))