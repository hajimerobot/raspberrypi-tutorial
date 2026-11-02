from gpiozero import AngularServo
import time

servo = AngularServo(13, min_pulse_width = 0.5/1000, min_angle = -90, \
                     max_pulse_width = 2.4/1000, max_angle = 90, \
                     frame_width = 20.0/1000)

try:
    while True:
        servo.angle = 0.0
        time.sleep(3)

        servo.angle = 90.0
        time.sleep(3)

        servo.angle = -90.0
        time.sleep(3)
except KeyboardInterrupt:
    pass

servo.angle = 0.0
time.sleep(3)

servo.close()
