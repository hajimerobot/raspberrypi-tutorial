import pigpio
import time

SERVO_PIN = 13

pi = pigpio.pi()

try:
    while True:
        # hardware_PWM( pin, frequency(Hz), dutycycle(0 to 1000000) )
        # 50Hz=20ms, Duty=1000000 x 1.45ms/20ms
        pi.hardware_PWM(SERVO_PIN, 50, int(1000000*1.45/20))
        time.sleep(3)
        # 50Hz=20ms, Duty=1000000 x 2.4ms/20ms
        pi.hardware_PWM(SERVO_PIN, 50, int(1000000*2.4/20))
        time.sleep(3)
        # 50Hz=20ms, Duty=1000000 x 0.5ms/20ms
        pi.hardware_PWM(SERVO_PIN, 50, int(1000000*0.5/20))
        time.sleep(3)
except KeyboardInterrupt:
    pass

# pi.set_servo_pulsewidth(SERVO_PIN, 0)
pi.hardware_PWM(SERVO_PIN, 50, 0)

pi.stop()
