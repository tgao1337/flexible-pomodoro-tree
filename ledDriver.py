'''I am assuming that each cluster of 7 LEDS will be on its own individual drivers, red is output A, 3 yellow is outputs B,C,D, 3 green is outputs E,F,G
I am assuming that the  last daisy chained driver will correspond to driver #4. '''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pins I am using for now
SER=14
RCLK=15
SRCLK=18
SRCLR= 23

NUM_CLUSTERS=4
NUM_COLORS=3
'''An array that of 12 integers that will account whether a given color group of LEDs is lit on a given cluster 
 the first three indices correspond to cluster 1, red, yellow , green and so on. 0 means offf, 1 is on. '''
clusterStatus=[0]*(NUM_CLUSTERS*NUM_COLORS)

# Global variables that will be passed into the drivers to light up a specfic color group.
GREEN_YELLOW_RED="01111111"
YELLOW_RED="00001111"
RED="00000001"
OFF= "00000000"

#setup the pins as outputs and set the clocks initally to low and the clear initially to high. 
def setup():
  GPIO.setup(SRCLR, GPIO.OUT)
  GPIO.setup(SER, GPIO.OUT)
  GPIO.setup(RCLK, GPIO.OUT)
  GPIO.setup(SRCLK, GPIO.OUT)

  GPIO.output(RCLK, GPIO.LOW)
  GPIO.output(SRCLK, GPIO.LOW)
  GPIO.output(SRCLR, GPIO.HIGH)
  clearAll()
#using the commonly connected SRCLR to all the drivers, pulsing RCLK while this is 0  will clear all drivers and LEDs oFF?.
def clearAll():
  GPIO.output(SRCLR, GPIO.LOW)
  GPIO.output(RCLK, GPIO.LOW)
  time.sleep(0.05)
  GPIO.output(RCLK, GPIO.HIGH)
  GPIO.output(SRCLR, GPIO.HIGH)

  for i in range(NUM_COLORS *NUM_CLUSTERS):
   clusterStatus[i]=0

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
Arguements: int cluster (1-4), char color( r,y,g)'''
def selectClusterColorON( cluster, color):
  #get current status of the LEDs
  cluster1= readClusterStatus(1)
  cluster2=readClusterStatus(2)
  cluster3=readClusterStatus(3)
  cluster4= readClusterStatus(4)
  newCluster=""

  #determine new string that will be passed into the desire cluster based on the color desired. 
  if(color=='g'):
   newCluster=GREEN_YELLOW_RED
  elif (color == 'y'):
   newCluster= YELLOW_RED
  elif (color == 'r'):
   newCluster=RED
  else:
    raise Exception("invalid color selection in selectClusterON(), choose g, y, r ")
  #keep the other clusters the same while updating the desired cluster LEDS
  if(cluster ==1):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(newCluster)
  elif(cluster ==2):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(newCluster)
    passToLEDs(cluster1)
  elif(cluster ==3):
    passToLEDs(cluster4)
    passToLEDs(newCluster)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  elif(cluster ==4):
    passToLEDs(newCluster)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  else:
     raise Exception("Number clusters invalid, must be an int>0 and less than NUM_CLUSTERS=",NUM_CLUSTERS)
# update the status array
  updateClusterStatus(cluster, True, color)
  display()

'''This function allows you to turn off a given color group of a given cluster
Arguements: int cluster (1-4), char color( r,y,g)'''
def selectClusterColorOFF( cluster, color):
  #get current status of the LEDs
  cluster1= readClusterStatus(1)
  cluster2=readClusterStatus(2)
  cluster3=readClusterStatus(3)
  cluster4= readClusterStatus(4)
  oldCluster=readClusterStatus(cluster)

  #determine new string that will be passed into the desire cluster based on the color desired off.
  if(color=='g'):
   newCluster=oldCluster[0]+"000"+oldCluster[4:]
  elif (color == 'y'):
   newCluster= oldCluster[:4]+"000"+oldCluster[7]
  elif (color == 'r'):
   newCluster=oldCluster[:7]+"0"
  else:
    raise Exception("invalid color selection in selectClusterON(), choose g, y, r ")
  #keep the other clusters the same while updating the desired cluster LEDS
  if(cluster ==1):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(newCluster)
  elif(cluster ==2):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(newCluster)
    passToLEDs(cluster1)
  elif(cluster ==3):
    passToLEDs(cluster4)
    passToLEDs(newCluster)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  elif(cluster ==4):
    passToLEDs(newCluster)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  else:
     raise Exception("Number clusters invalid, must be an int>0 and less than NUM_CLUSTERS=",NUM_CLUSTERS)
# update the status array
  updateClusterStatus(cluster, False, color)
  display()


'''This  function keeps track of changes made to  the clusters by updating the status array so that it is accurate.
Arugmetns: int cluster, bool on/off (T/F), char color( r,y,g,x) '''
def updateClusterStatus(cluster, on_off, color='x'):
  # find cluster's position in the array
  index=0
  index +=(cluster-1)*3
#this happens when updating an entire cluster to turn off, since I only pass in two parameters from the OFF() funcction. 
  if(color== 'x'):
   clusterStatus[index]=0
   clusterStatus[index+1]=0
   clusterStatus[index+2]=0
  else:  #updating a cluster with a new color being turned on or off
    if (color =='r'):
      pass     #the index is already in the position for the r index
    elif(color =='y'):
      index+=1
    elif(color =='g'):
      index+=2
    else:
      raise Exception("color error in updateCLusterStatus() use r,y,g")
    if(on_off):
      clusterStatus[index]=1
    else:
      clusterStatus[index]=0

'''This function iterates its way through the status array and generates an 8 bit binary 
representation of the actual LED sequence to be passed in to the seriel input of driver
Arugment: int cluster                 Returns: binary string'''
def readClusterStatus(cluster):
  start=(cluster-1)*3

  if(clusterStatus[start+2]==1): 
   return GREEN_YELLOW_RED
  elif(clusterStatus[start+1]==1):
   return YELLOW_RED
  elif(clusterStatus[start]==1):
   return RED
  else:
   return OFF

'''This function will turn off an entire cluster no matter which LEDS are currently on 
Arguments: int cluster'''
def selectClusterOFF(cluster):
  cluster1= readClusterStatus(1)
  cluster2=readClusterStatus(2)
  cluster3=readClusterStatus(3)
  cluster4= readClusterStatus(4)
  newCluster=OFF

  #keep the other clusters the same while updating the desired cluster  OFF
  if(cluster ==1):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(newCluster)
  elif(cluster ==2):
    passToLEDs(cluster4)
    passToLEDs(cluster3)
    passToLEDs(newCluster)
    passToLEDs(cluster1)
  elif(cluster ==3):
    passToLEDs(cluster4)
    passToLEDs(newCluster)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  elif(cluster ==4):
    passToLEDs(newCluster)
    passToLEDs(cluster3)
    passToLEDs(cluster2)
    passToLEDs(cluster1)
  else:
     raise Exception("Number clusters invalid, must be an int>0 and less than NUM_CLUSTERS=",NUM_CLUSTERS)

  updateClusterStatus(cluster, False)
  display()

#test code 

if __name__ == '__main__':
  setup()
  selectClusterColorON(1,'g')
  time.sleep(0.3)
  selectClusterColorON(2,'g')
  time.sleep(0.3)
  selectClusterColorON(3,'g')
  time.sleep(0.3)
  selectClusterOFF(2)
  time.sleep(0.3)
  selectClusterOFF(3)
  time.sleep(0.3)
  clearAll()

  #simulating the tree lighting up fully and then dimming fully 
  selectClusterColorON(1,'r')
  time.sleep(0.3)
  selectClusterColorON(2,'r')
  time.sleep(0.3)
  selectClusterColorON(3,'r')
  time.sleep(0.3)
  selectClusterColorON(1,'y')
  time.sleep(0.3)
  selectClusterColorON(2,'y')
  time.sleep(0.3)
  selectClusterColorON(3,'y')
  time.sleep(0.3)
  selectClusterColorON(1,'g')
  time.sleep(0.3)
  selectClusterColorON(2,'g')
  time.sleep(0.3)
  selectClusterColorON(3,'g')
  time.sleep(0.3)

# now starting to dim 
  selectClusterColorOFF(1,'g')
  time.sleep(0.3)
  selectClusterColorOFF(2,'g')
  time.sleep(0.3)
  selectClusterColorOFF(3,'g')
  time.sleep(0.3)
  selectClusterColorOFF(1,'y')
  time.sleep(0.3)
  selectClusterColorOFF(2,'y')
  time.sleep(0.3)
  selectClusterColorOFF(3,'y')
  time.sleep(0.3)
  selectClusterColorOFF(1,'r')
  time.sleep(0.3)
  selectClusterColorOFF(2,'r')
  time.sleep(0.3)
  selectClusterColorOFF(3,'r')
  time.sleep(0.3)
