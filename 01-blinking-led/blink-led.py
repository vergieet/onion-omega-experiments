import onionGpio
import time
import requests

sleepTime = 1

gpio0 = onionGpio.OnionGpio(0)
gpio0.setOutputDirection(0)

ledValue = 1
r="1"
while 1:
        if(r  == "1"):
                gpio0.setValue(1)
                r = "0"
        else:
                gpio0.setValue(0)
                r = "1"
        time.sleep(sleepTime)

