import RPi.GPIO as GPIO
import time

SW_PIN = 23
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(SW_PIN) == GPIO.HIGH:  # SW OFF
            GPIO.output(LED_PIN, GPIO.LOW)  # LED OFF
        else:  # SW ON
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON

        time.sleep(0.01)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
