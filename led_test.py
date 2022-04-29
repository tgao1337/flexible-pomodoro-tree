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
RCLK=8
SRCLK=11
SRCLR= 17

#setup the pins as outputs and set the clocks initally to low and the clear initially to high. 
def setup():
  spi.open(0,0)
  spi.mode=0b00
  spi.max_speed_hz= 7629

  GPIO.setup(RCLK, GPIO.IN) #set ce0 to input   
  GPIO.setup(SRCLR, GPIO.OUT) #set SRCLR as output and high
  GPIO.output(SRCLR, GPIO.HIGH)
#using the commonly connected SRCLR to all the drivers, pulsing RCLK while this is 0  will clear all drivers and LEDs oFF?.

def clearAll():
  GPIO.output(SRCLR, GPIO.LOW)
  spi.xfer([0b000000000])
  GPIO.output(SRCLR, GPIO.HIGH)

  for i in range(NUM_LEDS):
    ledList[i]=0

'''Given a certain string of 1010, this function will set the serial input and pulse the SRCLK and RCLK so the 
given pattern from the string is displayed corrrectly on the LEDS
Arguements: string clusterStatus'''
def passToLEDs(clusterStatus):
  for led in clusterStatus:
    if(led=="0"):
      GPIO.output(SER, GPIO.LOW)
    else:
     GPIO.output(SER, GPIO.HIGH)

    GPIO.output(SRCLK, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(SRCLK, GPIO.HIGH)

    
def displayLED():
  global ledList

  b1 = convertToBin(ledList[:24:-1])
  spi.xfer2([b1])
  spi.xfer2([convertToBin(ledList[24:16:-1])])
  spi.xfer2([convertToBin(ledList[16:7:-1])])
  spi.xfer2([convertToBin(ledList[7::-1])])
  '''GPIO.output(RCLK, GPIO.LOW) #pulse RCLK after all the inputs are loaded for a given cluster
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  '''
def convertToBin(lst):
  result = ""
  for i in lst:
    result += str(i)
  return int(result,2)

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

    
  
'''This is a recursive function which finds the first 0 in the LedDict and then updates the dict to turn that 
LED on. It starts at the first driver, which would be the lowest physically on the tree and looks to see if any
leds in any color groups are off and then moves onto the next one and next one.'''
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
'''This function turns all leds on'''
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
  time.sleep(2)  
  clearAll()
  print("CLEAR ALL")
  print(ledList)
  time.sleep(2)
  '''
  for i in range(24):
   time.sleep(2)
   toggleNextLed(1,True)
   print(ledList)
  

  for i in range(24):
   toggleNextLed(1,False)
  '''
  toggleNextLed(True,7)
  time.sleep(4)
  toggleNextLed(True,2)
  time.sleep(4)
  toggleNextLed(False,6)
  time.sleep(5)
  toggleNextLed(True,33)
  time.sleep(5)
  toggleNextLed(False,39)

'''
  toggleClusterColorGroup(1,'r',True)
  toggleClusterColorGroup(2,'r',True)
  toggleClusterColorGroup(3,'r',True)
  toggleClusterColorGroup(4,'r',True)
  print(ledDict)

  toggleClusterColorGroup(1,'y',True)
  toggleClusterColorGroup(2,'y',True)
  toggleClusterColorGroup(3,'y',True)
  toggleClusterColorGroup(4,'y',True)
  print(ledDict)

  toggleClusterColorGroup(1,'g',True)
  toggleClusterColorGroup(2,'g',True)
  toggleClusterColorGroup(3,'g',True)
  toggleClusterColorGroup(4,'g',True)
  print(ledDict)

  toggleClusterColorGroup(1,'g',False)
  toggleClusterColorGroup(2,'g',False)
  toggleClusterColorGroup(3,'g',False)
  toggleClusterColorGroup(4,'g',False)
  print(ledDict)

  toggleClusterColorGroup(1,'y',False)
  toggleClusterColorGroup(2,'y',False)
  toggleClusterColorGroup(3,'y',False)
  toggleClusterColorGroup(4,'y',False)
  print(ledDict)

  toggleClusterColorGroup(1,'r',False)
  toggleClusterColorGroup(2,'r',False)
  toggleClusterColorGroup(3,'r',False)
  toggleClusterColorGroup(4,'r',False)
  print(ledDict)

  toggleClusterColorGroup(2,'y',True)
  toggleNextLed(False)
  toggleNextLed(True)
  toggleNextLed(True)
  toggleNextLed(False)
  toggleClusterColorGroup(1,'y',True)
  toggleNextLed(False)
  toggleClusterColorGroup(3,'r',True)
  toggleNextLed(False)
  toggleClusterColorGroup(2,'g',True)
  allOn()
  selectClusterOFF(2)
  selectClusterOFF(4)
  selectClusterOFF(3)
  toggleNextLed(True)
  selectClusterOFF(1)
'''

