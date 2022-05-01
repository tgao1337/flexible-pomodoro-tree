import RPi.GPIO as GPIO
import time

rest = 0
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523
D5 = 587
E5 = 659
F5 = 698
G5 = 784
A5 = 880
B5 = 988
C6 = 1047
D6 = 1175
E6 = 1319
F6 = 1397
G6 = 1568
A6 = 1760
B6 = 1976
C7 = 2093
D7 = 2349
E7 = 2637
F7 = 2794
G7 = 3136
A7 = 3520
B7 = 3951
C8 = 4186

pinnum = 12

def buzzerSetup(pin):
  GPIO.setmode(GPIO.BCM)
  global pinnum
  pinnum = pin
  GPIO.setup(pinnum, GPIO.OUT) # This sets pin number from parameters as an output

def playTime(seconds):
  # This will play the buzzer at the default 4kHz for 
  # (seconds) amount of seconds.

  # first arg is pin number, second is frequency in Hz
  pwm_out = GPIO.PWM(pinnum, 4000) # The default 4000 Hz can be changed
  # argument is duty cycle, out of 100 parts
  pwm_out.start(50) # 50/100 is most efficient for a piezo buzzer
  # observe output
  time.sleep(seconds) # This will end after given seconds
  
def playFreq(freq):
  # This will play buzzer at a given frequency. It will not be stopped unless playStop() is used.

  pwm_out = GPIO.PWM(pinnum, freq)
  pwm_out.start(50)
  time.sleep(1)
  
def playStop():
  # This will stop any buzzer sounds.
  
  pwm_out = GPIO.PWM(pinnum, 0)
  pwm_out.start(0)
  time.sleep(1)
  
def playFreqTime(freq, seconds):
  # This function plays a specified frequency for a specified time.
  # freq=0 is for a rest note.

  if freq == 0:
   pwm_out = GPIO.PWM(pinnum, 0)
    pwm_out.start(0)
  else:
    pwm_out = GPIO.PWM(pinnum, freq)
    pwm_out.start(50)
  time.sleep(seconds)
  pi.hardware_PWM(13, freq, 0)
  
def playList(lst):
  # Given a list of [(freq, seconds), (freq, seconds), ... ], play through the list
  # list also works as ((freq, seconds), (freq, seconds), ... )

  for elem in lst:
    playFreqTime(elem[0], elem[1])

buzzerSetup(12)
playFreqTime(A7, .5)
