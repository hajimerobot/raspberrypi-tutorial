from gpiozero import DigitalOutputDevice
import time

led_r = DigitalOutputDevice(17)
led_g = DigitalOutputDevice(27)
led_b = DigitalOutputDevice(22)

led_r.on()
led_g.off()
led_b.off()
time.sleep(1)

led_r.off()
led_g.on()
led_b.off()
time.sleep(1)

led_r.on()
led_g.on()
led_b.off()
time.sleep(1)

led_r.off()
led_g.off()
led_b.on()
time.sleep(1)

led_r.on()
led_g.off()
led_b.on()
time.sleep(1)

led_r.off()
led_g.on()
led_b.on()
time.sleep(1)

led_r.on()
led_g.on()
led_b.on()
time.sleep(1)
