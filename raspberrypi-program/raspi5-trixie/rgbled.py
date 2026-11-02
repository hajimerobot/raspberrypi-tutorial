from gpiozero import DigitalOutputDevice

led_r = DigitalOutputDevice(17)
led_g = DigitalOutputDevice(27)
led_b = DigitalOutputDevice(22)

led_r.on()
led_g.off()
led_b.off()
