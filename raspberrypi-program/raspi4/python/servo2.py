import pigpio
import time

SERVO_PIN = 13

pi = pigpio.pi()

try:
    while True:
        pi.set_servo_pulsewidth(SERVO_PIN, 1450)
        time.sleep(3)
        pi.set_servo_pulsewidth(SERVO_PIN, 2400)
        time.sleep(3)
        pi.set_servo_pulsewidth(SERVO_PIN, 500)
        time.sleep(3)
except KeyboardInterrupt:
    pass

pi.set_servo_pulsewidth(SERVO_PIN, 0)
pi.stop()
