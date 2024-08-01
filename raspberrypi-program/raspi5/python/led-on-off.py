from gpiozero import LED
import time

myled = LED(17)
myled.on()
time.sleep(2)
myled.off()
