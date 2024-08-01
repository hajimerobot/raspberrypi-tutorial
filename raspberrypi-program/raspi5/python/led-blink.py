from gpiozero import LED
import time

myled = LED(17)

while True:
    myled.on()
    time.sleep(0.5)
    myled.off()
    time.sleep(0.5)
