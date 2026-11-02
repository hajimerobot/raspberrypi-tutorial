from gpiozero import LED
import time

myled = LED(17)

for i in range(10):
    myled.on()
    time.sleep(0.5)
    myled.off()
    time.sleep(0.5)
