import time
from plyer import notification
times=float(input("set the second after you want to drink Water"))
while (True):
    time.sleep(times)
    notification.notify(title="Water",message="you should drink water",timeout=2) 