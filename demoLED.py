# basic demo of LED driver

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pins I am using for now
SER=14
RCLK=15
SRCLK=18
SRCLR= 23

NUM_LEDS=8

def setup():
  GPIO.setup(SRCLR, GPIO.OUT)
  GPIO.setup(SER, GPIO.OUT)
  GPIO.setup(RCLK, GPIO.OUT)
  GPIO.setup(SRCLK, GPIO.OUT)

  GPIO.output(RCLK, GPIO.LOW)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(SRCLR, GPIO.HIGH)

'''Tells which leds to turn on or off'''
def passToLEDs(outputString):

  for led in outputString:
    if(led=="0"):
      GPIO.output(SER, GPIO.LOW)
    else:
     GPIO.output(SER, GPIO.HIGH)

    GPIO.output(SRCLK, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(SRCLK, GPIO.HIGH)

  GPIO.output(RCLK, GPIO.LOW) #pulse RCLK after all the inputs are loaded
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)

''' Pass in LED # to turn on.LED 0 is output A of first driver. '''
def turnOnSingleLed(num)
   if (num<NUM_LEDS):
     output=""
    for i in range(NUM_LEDS):
      if i=num:
        output+="1"
      else:
        output+="0"
    passToLEDs(output[::-1])
   else:
    raise Exception("LED passed in exceeds number of LEDs available")

def turnAllOn():
  output=""
  for i in range(NUM_LEDS):
   output+="1"
  passToLEDs(output)

def turnAllOff():
  GPIO.output(SRCLR, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(SRCLR, GPIO.HIGH)

'''Turn on entire driver LEDs by specifying driver sequence in chain. 1 is the first driver'''
def turnOnEntireDriver(num):
  output=""
  if(num*8 <= NUM_LEDS):
   for i in range(NUM_LEDS):
    if (i >=num*8 -8 and i< num *8)
      output+="1"
    else:
      output+="0" 
   passToLEDS(output[::-1])
  else:
   raise Exception("Driver specified exceeds numver of available LEDs")

'''Pass in the desired amount of OFF LEDs you want in between the ON LEDs'''
def turnOnLEDsWithSpacing(num):
  if(num >NUM_LEDS):
    turnAllOff()
  else if(num ==0):
    turnAllOn()
  else:
   output=""
   for i in range(NUM_LEDS):
    if (i %(num+1)==0):
      output+="1"
    else:
      output+="0"
  passToLEDs(output[::-1])
