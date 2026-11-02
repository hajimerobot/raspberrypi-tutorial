from gpiozero import PWMOutputDevice
import time
import random

led_r = PWMOutputDevice(17)
led_g = PWMOutputDevice(27)
led_b = PWMOutputDevice(22)

for i in range(10):
# while True:
    led_r.value = random.random()
    led_g.value = random.random()
    led_b.value = random.random()

    time.sleep(1)
