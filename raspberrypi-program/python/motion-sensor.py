import RPi.GPIO as GPIO
import time

PIR_PIN = 24
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
