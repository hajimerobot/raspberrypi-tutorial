import RPi.GPIO as GPIO
import time

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

p_red = GPIO.PWM(RED_PIN, 100)  # Hz
p_green = GPIO.PWM(GREEN_PIN, 100)  # Hz
p_blue = GPIO.PWM(BLUE_PIN, 100)  # Hz

p_red.start(100)  # duty(0-100)
p_green.start(10)  # duty(0-100)
p_blue.start(10)  # duty(0-100)

time.sleep(5)

p_red.stop()
p_green.stop()
p_blue.stop()

GPIO.cleanup()
