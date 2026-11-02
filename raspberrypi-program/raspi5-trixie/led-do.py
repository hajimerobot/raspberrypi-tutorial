from gpiozero import DigitalOutputDevice
import time

myled = DigitalOutputDevice(17)
myled.on()
time.sleep(2)
myled.off()
