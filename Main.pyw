from Pinger import Pinger
from Toast import *
from Wifi import Wifi
import time

wifi = Wifi()
pinger = Pinger()
unstableTime = 0

while True:
    if pinger.isConnectionUnstable():
        try:
            if unstableTime == 0 or unstableTime == 2:
                sayReconnect()
                wifi.disconnect()
                time.sleep(2)
                wifi.connect()
            if unstableTime >3:
                sayCheck()
        finally:
            unstableTime += 1
            time.sleep(5)
    else:
        if unstableTime == 0:
            time.sleep(30)
        else:
            sayConnectSuccess()
            unstableTime = 0
            time.sleep(15)
