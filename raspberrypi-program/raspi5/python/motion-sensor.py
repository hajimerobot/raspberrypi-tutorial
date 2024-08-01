from gpiozero import DigitalInputDevice, LED
import time

pir = DigitalInputDevice(24, pull_up = None, active_state = True)

myled = LED(17)

while True:
    if pir.is_active:
        myled.on()
    else:
        myled.off()

    time.sleep(0.1)
