import pigpio
import time

def playTime(seconds):
  pi = pigpio.pi()
  # first arg is pin number,
  # second arg is frequency in Hz,
  # third arg is number of ON units out of 1000000
  pi.hardware_PWM(13, 4000, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, 4000, 0)
  
def playFreq(freq):
  pi = pigpio.pi()
  # first arg is pin number,
  # second arg is frequency in Hz,
  # third arg is number of ON units out of 1000000
  pi.hardware_PWM(13, freq, 500000) 
  time.sleep(0.5)
  pi.hardware_PWM(13, freq, 0)
  
def playFreqTime(freq, seconds):
  pi = pigpio.pi()
  # first arg is pin number,
  # second arg is frequency in Hz,
  # third arg is number of ON units out of 1000000
  pi.hardware_PWM(13, freq, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, freq, 0)

