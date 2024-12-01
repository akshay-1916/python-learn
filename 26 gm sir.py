import time
t=time.strftime("%H:%M:%S")
print(t)
hour=int(time.strftime("%H"))
print(hour)

if(hour>0 and hour<12):
    print("Morning")
    
if(hour>12 and hour<17):
    print("Afternoon")
    
if(hour>17 and hour<24):
    print("night")        