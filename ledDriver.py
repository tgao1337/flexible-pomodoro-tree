'''I am assuming that each cluster of 7 LEDS will be on its own individual drivers, red is output A, 3 yellow is outputs B,C,D, 3 green is outputs E,F,G
I am assuming that the  last daisy chained driver will correspond to driver #4. '''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pins I am using for now
SER=10
RCLK=8
SRCLK=11
SRCLR= 17

NUM_CLUSTERS=4
NUM_COLORS=3

ledDict= {}
ledDict["r1"]=[0]
ledDict["y1"]=[0,0,0]
ledDict["g1"]=[0,0,0]
ledDict["r2"]=[0]
ledDict["y2"]=[0,0,0]
ledDict["g2"]=[0,0,0]
ledDict["r3"]=[0]
ledDict["y3"]=[0,0,0]
ledDict["g3"]=[0,0,0]
ledDict["r4"]=[0]
ledDict["y4"]=[0,0,0]
ledDict["g4"]=[0,0,0]


#setup the pins as outputs and set the clocks initally to low and the clear initially to high. 
def setup():
  GPIO.setup(SRCLR, GPIO.OUT)
  GPIO.setup(SER, GPIO.OUT)
  GPIO.setup(RCLK, GPIO.OUT)
  GPIO.setup(SRCLK, GPIO.OUT)

  GPIO.output(RCLK, GPIO.LOW)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(SRCLR, GPIO.HIGH)

#using the commonly connected SRCLR to all the drivers, pulsing RCLK while this is 0  will clear all drivers and LEDs oFF?.
def clearAll():
  GPIO.output(SRCLR, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(SRCLR, GPIO.HIGH)

  for key in ledDict:
   if "r" in key:
      ledDict[key]=[0]
   else:
      ledDict[key]=[0,0,0]

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

def display():
  GPIO.output(RCLK, GPIO.LOW) #pulse RCLK after all the inputs are loaded for a given cluster
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)

'''This function allows you to turn on a given color group of a given cluster
Arguements: int cluster (1-4), char color( r,y,g), bool on or off '''
def toggleClusterColorGroup( cluster,color,turnOn):

  if (color != 'r' and color != 'y' and color != 'g'):
    raise Exception("invalid color selection in ClusterColorON(), choose'g', 'y', 'r' ")
  if(cluster <1  or  cluster >NUM_CLUSTERS):
    raise Exception("Number clusters invalid, must be an int>0 and less than NUM_CLUSTERS=",NUM_CLUSTERS)
  if(turnOn):
   updateClusterStatus(cluster,True,color,True)
  else:
   updateClusterStatus(cluster,True,color,False)

  for i in range(NUM_CLUSTERS,0,-1):
   passToLEDs(readClusterStatus(i))

  display()

'''This function allows you to turn on the lowest currently off led in the chain or turn off the highedst currently on led in the chain
Arguements: bool on or off'''
def toggleNextLed(turnOn):

  if(turnOn):
    if(not (findNextLedToUpdateOn())):
     print("ALL LEDS ON ALREADY\n")
  else:
   if(not(findNextLedToUpdateOff())):
    print("ALL LEDS OFF ALREADY\n")

  for i in range(NUM_CLUSTERS,0,-1):
   passToLEDs(readClusterStatus(i))

  display()
'''This function (not to be called) will update the ledDict based on what led/s have turned on/off. 
If we wanted we could call any led from here to see if there is something wrong with it. 
Arugments: int cluster, bool turnWholeClusterOn, char color, bool turnLedOn'''
def updateClusterStatus(cluster,turnWholeClusterOn,color,turnLedOn):
  if (color != 'r' and color != 'y' and color != 'g'):
   raise Exception( "Need to pass r,y,g in updateDictionary()")

  key= color + str(cluster)

  if (color=='r'):
    if (turnLedOn):
       ledDict[key]=[1]
    else:
      ledDict[key]=[0]

  elif(turnWholeClusterOn):  # entire cluster is turned off or on
    if(turnLedOn):
      ledDict[key]=[1,1,1]
    else:
      ledDict[key]=[0,0,0]

  else:  # find the led that needs to be updated on or off 
    if(turnLedOn):
       findNextLedToUpdateOn(key)
    else:
       findNextLedToUpdateOff(key)
'''This is a recursive function which finds the first 0 in the LedDict and then updates the dict to turn that 
LED on. It starts at the first driver, which would be the lowest physically on the tree and looks to see if any
leds in any color groups are off and then moves onto the next one and next one.'''
def findNextLedToUpdateOn(key="x"):
  if (key != "x"): 
   found=False
   arr=ledDict.get(key)
   for i in range(3):
      if(arr[i]==0):
        arr[i]=1
        found=True
        break
   ledDict[key]=arr
   return found
  else:
   for i in range (1,NUM_CLUSTERS+1):
      redKey = "r"+str(i)
      yelKey= "y"+str(i)
      grKey= "g" + str(i)
      if(ledDict.get(redKey)[0]==0):
         ledDict[redKey]=[1]
         return True
      if(findNextLedToUpdateOn(yelKey)):
          return True
      if(findNextLedToUpdateOn(grKey)):
          return True
   return False

'''This is a recursive function which finds the first 1 in the LedDict and then updates the dict to turn that
LED off. It starts at the fourth driver, which would be the highest physically on the tree and looks to see if any
leds in any color groups are on and then moves onto the lower one and so on.'''
def findNextLedToUpdateOff(key="x"):
  if (key !="x"):
   found=False
   arr=ledDict.get(key)
   for i in range( 2, -1, -1):
        if (arr[i]==1):
          arr[i]=0
          found=True
          break
   ledDict[key]=arr
   return found
  else:
   for i in range (NUM_CLUSTERS,0,-1):
      redKey = "r"+str(i)
      yelKey= "y"+str(i)
      grKey= "g" + str(i)
      
      if(findNextLedToUpdateOff(grKey)):
          return True
      if(findNextLedToUpdateOff(yelKey)):
          return True
      if(ledDict.get(redKey)[0]==1):
         ledDict[redKey]=[0]
         return True
   return False
'''This function reads the ledDict and generates an 8 bit binary string for the current state of the 
LEDs. The string is the returned in the reverse since the drivers need to be inputted that way
Arguments: int cluster'''
def readClusterStatus(cluster):
  redKey = "r"+str(cluster)
  yelKey= "y"+str(cluster)
  grKey= "g" + str(cluster)

  status=""
  status += str(ledDict.get(redKey)[0])

  for led in ledDict.get(yelKey):
    status +=str(led)
 
  for led in ledDict.get(grKey):
    status +=str(led)

  status +="0"

  return status[::-1]


'''This function will turn off an entire cluster no matter which LEDS are currently on 
Arguments: int cluster'''
def selectClusterOFF(cluster):

  if(cluster <1 or cluster >NUM_CLUSTERS):
   raise Exception("Number clusters invalid, must be an int>0 and less than NUM_CLUSTERS=",NUM_CLUSTERS)
  
  updateClusterStatus(cluster,True,'r',False)
  updateClusterStatus(cluster,True,'y',False)
  updateClusterStatus(cluster,True,'g',False)

  for i in range(NUM_CLUSTERS,0,-1):
   passToLEDs(readClusterStatus(i))

  display()
'''This function turns on all LEDs'''
def allOn():

  
  for i in range(NUM_CLUSTERS,0,-1):
   passToLEDs("11111111")
  
  display()
  time.sleep(2)

#test code
if __name__ == '__main__':
  setup()

  allOn()
  time.sleep(0.05)  
  clearAll()
  print(ledDict)
  
  for i in range(24):
   toggleNextLed(True)
   print(ledDict)
  clearAll()

  for i in range(24):
   toggleNextLed(False)


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
