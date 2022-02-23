import pigpio
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
E6 = 1382
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

def buzzerSetup():
  global pi = pigpio.pi()

def playTime(seconds):
  # This will play the buzzer at the default 4kHz for 
  # (seconds) amount of seconds.

  # first arg is pin number,
  # second arg is frequency in Hz,
  # third arg is number of ON units out of 1000000
  pi.hardware_PWM(13, 4000, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, 4000, 0)
  
def playFreq(freq):
  # This will play buzzer at a given frequency for 0.5 seconds.

  pi.hardware_PWM(13, freq, 500000) 
  time.sleep(0.5)
  pi.hardware_PWM(13, freq, 0)
  
def playFreqTime(freq, seconds):
  # This function plays a specified frequency for a specified time.
  # freq=0 is for a rest note.

  if freq == 0:
   pi.hardware_PWM(13, freq, 0)
  else:
    pi.hardware_PWM(13, freq, 500000) 
  time.sleep(seconds)
  pi.hardware_PWM(13, freq, 0)
  
def playList(lst):
  # Given a list of ((freq, seconds), (freq, seconds), ... ), play through the list
  for elem in lst:
    playFreqTime(elem[0], elem[1])

