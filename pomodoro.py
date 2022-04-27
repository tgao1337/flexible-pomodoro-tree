# This will be the foo.py in the example slides Professor Fund showed.
import pigpio
import time
import RPi.GPIO as GPIO
from smbus import SMBus
# from PIL import Image,ImageDraw,ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

serial = i2c(port=1, address = 0x3C)
device = sh1106(serial)

default_font = ImageFont.truetype('Font.ttf', 10)
OLED_WIDTH = 128
OLED_HEIGHT = 64

# Create a new blank canvas
canvas = Image.new('1', (OLED_WIDTH, OLED_HEIGHT), 255)
# Set up draw for the canvas
draw = ImageDraw.Draw(canvas)

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Buttons
#pinA = 4
pinA = 5
pinB = 6
pinC = 16
pinD = 24
pinE = 26
GPIO.setup(pinA, GPIO.IN)
GPIO.setup(pinB, GPIO.IN)
GPIO.setup(pinC, GPIO.IN)
GPIO.setup(pinD, GPIO.IN)
GPIO.setup(pinE, GPIO.IN)
#GPIO.setup(pinF, GPIO.IN)

# Pins used for driver
SER = 10
RCLK = 8
SRCLK = 11
SRCLR = 17

NUM_CLUSTERS = 4

# Creating dictionary to store current status of leds
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

# This section begins the buzzer subsystem for hardware PWM.
# Software PWM is a potential for simplicity.
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

def buzzerSetup():
  global pi 
  pi = pigpio.pi()

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
  # This will play buzzer at a given frequency. It will not be stopped unless playStop() is used.

  pi.hardware_PWM(13, freq, 500000)
  
def playStop():
  # This will stop any buzzer sounds.
  
  pi.hardware_PWM(13, 0, 0)
  
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
  # Given a list of [(freq, seconds), (freq, seconds), ... ], play through the list
  # list also works as ((freq, seconds), (freq, seconds), ... )

  for elem in lst:
    playFreqTime(elem[0], elem[1])
    
# This section is for...

'''
class OLED(object):
    def __init__(self):
        self.width = OLED_WIDTH
        self.height = OLED_HEIGHT
        self.address = 0x3c
        self.bus = SMBus(1)

    def write(self, cmd):
        # Writing to I2C
        self.bus.write_byte_data(self.address, 0x00, cmd)

    def setup(self):
        # Initialize display
        self.write(0xAE)	# Turn off OLED panel
        self.write(0x02)	# Set Lower Column Address
        self.write(0x10)	# Set Higher Column address
        self.write(0x40)	# Set Display Start Line
        self.write(0x81)	# Set Contrast Control Mode
        self.write(0xA0)	# Set Segment Re-map
        self.write(0xC0)	# Set Common Output Scan Direction
        self.write(0xA6)	# Set Normal Display
        self.write(0xA8)	# Set Multiplex Ration Mode
        self.write(0x3F)	# Set Multiplex Ration Data: ratio 64
        self.write(0xD3)	# Set Display Offset Mode
        self.write(0x00)	# Set Display Offset Data: 0
        self.write(0xD5)	# Set Divide Ratio/Oscillator Frequency Mode
        self.write(0x80)	# Set Divide Ratio/Oscillator Frequency Data
        self.write(0xD9)	# Set Pre-charge Period Mode
        self.write(0xF1)	# Set Pre-Charge Period As 15 Clocks & Discharge Period as 1 Clock
        self.write(0xDA)	# Set Common Pads Hardware Configuration Mode
        self.write(0x12)        # Set Sequential/Alternative Mode
        self.write(0xDB)	# Set VCOM Deselect Level Mode Set
        self.write(0x40)	# Set VCOM Deselect Level Data
        self.write(0x20)	# Set Page Addressing Mode
        self.write(0xA4)	# Set Entire Display Off
        time.sleep(0.1)
        self.write(0xAF)	# Turn on OLED panel


    def getbuffer(self, image):
        buf = [0xFF] * ((self.width//8) * self.height)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()

        if(imwidth == self.width and imheight == self.height):
            for y in range(imheight):
                for x in range(imwidth):
                    if pixels[x, y] == 0:
                        buf[x + (y // 8) * self.width] &= ~(1 << (y % 8))

        elif(imwidth == self.height and imheight == self.width):
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[(newx + (newy // 8 )*self.width) ] &= ~(1 << (y % 8))
        return buf

    def ShowImage(self, pBuf):
        for page in range(0,8):
            self.write(0xB0 + page);
            self.write(0x02);
            self.write(0x10);
            for i in range(0, self.width):
                self.bus.write_byte_data(self.address, 0x40, ~pBuf[i+self.width*page])

    def clear(self):
        # Clearing the buffer / display
        _buffer = [0xff]*(self.width * self.height//8)
        self.ShowImage(_buffer)
        # Clearing the canvas
        draw.rectangle((0,0,128,64), outline=255, fill=255) 

    # Functions for displaying on OLED
    def text(self, text, x, y, size=10):
        font = ImageFont.truetype("Font.ttf", size)
        draw.text ((x,y), text, font=font, fill=0)
        self.show()

    def show(self):
        self.ShowImage(self.getbuffer(canvas.rotate(180)))

    def draw_line(self, w, x, y ,z):
        # From (w,x) to (y,x)
        draw.line([(w,x),(y,z)])
        self.show()
'''
#LED driver functions 
def led_setup():
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

def allOn():
  
  for i in range(NUM_CLUSTERS,0,-1):
   passToLEDs("11111111")
  
  display()
  time.sleep(2)
  
# Returns the state of button at given pin
def readButton(pin):
  return GPIO.input(pin)

with canvas(device) as draw:
    draw.draw_line((0, 45, 127 ,45), fill="white")
    draw.text((40, 43), "Welcome", fill="white")
