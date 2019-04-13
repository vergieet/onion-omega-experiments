import onionGpio
import time
import subprocess
sleepTime = 2

gpio0 = onionGpio.OnionGpio(0)
gpio0.setOutputDirection(0)

ledValue = 1
r="1"
while 1:
        gpio0.setValue(0)
        cmd = "nfc-list | grep UID | sed -e 's/ //g' -e 's/^.*://'"
        uid = subprocess.check_output(cmd,shell=True).rstrip('\n')
        if(uid  != ""):
                gpio0.setValue(1)
                time.sleep(sleepTime)
