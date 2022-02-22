import pigpio
import time

def playTime(seconds):
  # This will play the buzzer at the default 4kHz for 
  # (seconds) amount of seconds.
  pi = pigpio.pi()
  # first arg is pin number,
  # second arg is frequency in Hz,
  # third arg is number of ON units out of 1000000
  pi.hardware_PWM(13, 4000, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, 4000, 0)
  
def playFreq(freq):
  # This will play buzzer at a given frequency for 0.5 seconds.
  pi = pigpio.pi()
  pi.hardware_PWM(13, freq, 500000) 
  time.sleep(0.5)
  pi.hardware_PWM(13, freq, 0)
  
def playFreqTime(freq, seconds):
  # This function plays a specified frequency for a specified time.
  pi = pigpio.pi()
  if freq == 0:
   pi.hardware_PWM(13, freq, 0)
  else:
    pi.hardware_PWM(13, freq, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, freq, 0)

