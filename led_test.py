import RPi.GPIO as GPIO
import spidev
import time

GPIO.setmode(GPIO.BCM)

NUM_LEDS= 32
global available_led
available_led = NUM_LEDS

global ledList
ledList= [0] * NUM_LEDS

spi=spidev.SpiDev()
SER=10
RCLK=18
SRCLK=11
SRCLR= 17

#setup the pins as outputs and set the clocks initally to low and the clear initially to high. 
def setup():
  spi.open(0,0)
  spi.mode=0b00
  spi.max_speed_hz= 7629

  GPIO.setup(RCLK, GPIO.OUT) #set RCLK to output
  GPIO.output(RCLK,GPIO.LOW)
  GPIO.setup(SRCLR, GPIO.OUT) #set SRCLR as output and high
  GPIO.output(SRCLR, GPIO.HIGH)
#using the commonly connected SRCLR to all the drivers, pulsing RCLK while this is 0  will clear all drivers and LEDs oFF?.

def clearAll():
  GPIO.output(SRCLR, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(SRCLR, GPIO.HIGH)

  for i in range(NUM_LEDS):
    ledList[i]=0

    
def displayLED():
  global ledList
  
  hex=hexList()
  print("HEX", hex)
  GPIO.output(RCLK, GPIO.LOW)
  spi.xfer(hex)
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  

def hexList():
  byte = ""
  i = 1
  hexLEDList = []
  for bit in ledList:
    byte += str(bit)
    if (i%8 == 0):
      byte = byte[::-1]
      hexLEDList.append(hex(int(byte,2)))
      byte = ""
    i+=1
  return hexLEDList
      
  
  
  


'''This function allows you to turn on the lowest currently off led in the chain or turn off the highedst currently on led in the chain
Arguements: bool on or off'''
def toggleNextLed(turnOn,amount=1):
  global available_led
  global ledList
  print("in toggle")
  ledNum= findNextLed(turnOn)
  print("Led found is ", ledNum)
  if(ledNum != -1):
    if turnOn:
      if amount > available_led:
        for i in range(ledNum,NUM_LEDS):
          ledList[i]=1
        available_led =0
        print("O N: amnt ",amount, " available ", available_led)
      else:
        for i in range(ledNum,ledNum+amount):
          ledList[i] =1
        available_led -= amount
        print("ON: amnt ",amount, " available ", available_led)
    else:
      if amount > (NUM_LEDS-available_led):
        for i in range(ledNum,-1,-1):
          ledList[i]=0
        available_led =NUM_LEDS
        print("O FF: amnt ",amount, " available ", available_led)
      else:
        for i in range(ledNum,ledNum-amount,-1):
          ledList[i] =0
        available_led += amount
        print("OFF: amnt ",amount, " available ", available_led)

    displayLED()

def findNextLed(turnOn):
  global ledList
  ind=0
  try:
    if turnOn:
      ind= ledList.index(0)
    else:
      ind= NUM_LEDS - 1 - ledList[::-1].index(1)
  except ValueError as e:
      print("NOT FOUND")
  return ind
              

  
'''This function turns on all LEDs'''
def allOn():

  for i in range(NUM_LEDS):
    ledList[i]=1
  print("IN ALL ON, disp List:", ledList)
  displayLED()
  

#test code
if __name__ == '__main__':
  setup()

  allOn()
  print("ALLON")
  time.sleep(5)  
  clearAll()
  print("CLEAR ALL")
  print(ledList)
  time.sleep(5)
  
  for i in range(32):
   time.sleep(2)
   toggleNextLed(1,True)
   print(ledList)
  

  for i in range(32):
   toggleNextLed(1,False)
  
  toggleNextLed(4, True)
  time.sleep(1)
  toggleNextLed(8,True)
  time.sleep(1)
  toggleNextLed(15,False)
  time.sleep(1)
  toggleNextLed(22,True)
  time.sleep(1)
  toggleNextLed(13, False)

