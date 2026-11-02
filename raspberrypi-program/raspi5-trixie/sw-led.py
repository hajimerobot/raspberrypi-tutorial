from gpiozero import Button, LED
import time

btn = Button(23, pull_up = True)

myled = LED(17)

while True:
    if btn.is_pressed:
        myled.on()
    else:
        myled.off()

    time.sleep(0.01)
