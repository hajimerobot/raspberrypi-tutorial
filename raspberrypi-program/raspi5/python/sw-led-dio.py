from gpiozero import DigitalInputDevice, DigitalOutputDevice
import time

btn = DigitalInputDevice(23, pull_up = True)

myled = DigitalOutputDevice(17)

while True:
    if btn.is_active:
        myled.on()
    else:
        myled.off()

    time.sleep(0.01)
