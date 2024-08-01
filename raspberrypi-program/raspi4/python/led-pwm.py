import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

p = GPIO.PWM(LED_PIN, 1)  # Hz

p.start(50)  # duty(0-100)

time.sleep(5)

p.stop()

GPIO.cleanup()
