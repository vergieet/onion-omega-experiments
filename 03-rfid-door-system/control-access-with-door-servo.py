from motors import Servo
import onionGpio
import time
import subprocess

sleepTime = 2

gpio0 = onionGpio.OnionGpio(0)
gpio0.setOutputDirection(0)


microServo = Servo(1, 500, 2400)
microServo.setAngle(0.0)
gpio0.setValue(0)
while 1:
        cmd = "nfc-list | grep UID | sed -e 's/ //g' -e 's/^.*://'"
        uid = subprocess.check_output(cmd,shell=True).rstrip('\n')
        if(uid  != ""):
                gpio0.setValue(1)
                microServo.setAngle(180.0)
                time.sleep(sleepTime)
                gpio0.setValue(0)
                microServo.setAngle(0.0)
                time.sleep(sleepTime)
