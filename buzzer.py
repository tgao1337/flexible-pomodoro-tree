import pigpio
import time

pi = pigpio.pi()
# first arg is pin number,
# second arg is frequency in Hz,
# third arg is number of ON units out of 1000000
pi.hardware_PWM(13, 4000, 500000) 

time.sleep(2)
