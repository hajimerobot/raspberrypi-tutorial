from gpiozero import PWMOutputDevice
import time

myled = PWMOutputDevice(17, frequency = 1)

myled.value = 0.5  # duty(0-1)

time.sleep(3)

myled.close()
