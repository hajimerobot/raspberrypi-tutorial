import pigpio
import time

SERVO_PIN = 13

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO_PIN, 1450)
# pi.set_servo_pulsewidth(SERVO_PIN, 2400)
# pi.set_servo_pulsewidth(SERVO_PIN, 500)
time.sleep(3)
pi.set_servo_pulsewidth(SERVO_PIN, 0)

pi.stop()
