import RPi.GPIO as GPIO
import time

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.HIGH)
GPIO.output(BLUE_PIN, GPIO.LOW)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.HIGH)
GPIO.output(BLUE_PIN, GPIO.LOW)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.HIGH)
GPIO.output(BLUE_PIN, GPIO.HIGH)
time.sleep(1)

GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.HIGH)
GPIO.output(BLUE_PIN, GPIO.HIGH)
time.sleep(1)

GPIO.cleanup()
