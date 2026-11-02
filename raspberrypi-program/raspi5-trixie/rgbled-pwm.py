from gpiozero import PWMOutputDevice

led_r = PWMOutputDevice(17)
led_g = PWMOutputDevice(27)
led_b = PWMOutputDevice(22)

led_r.value = 1
led_g.value = 0.1
led_b.value = 0.1
