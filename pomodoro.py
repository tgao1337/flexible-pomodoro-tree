# This will be the foo.py in the example slides Professor Fund showed.
import time
import RPi.GPIO as GPIO
from smbus import SMBus
# from PIL import Image,ImageDraw,ImageFont
from PIL import ImageFont, Image
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
import spidev

serial = i2c(port=1, address = 0x3C)
device = sh1106(serial)

fontBig = ImageFont.truetype('Font.ttf', 25)
fontSmall = ImageFont.truetype('Font.ttf', 12)
OLED_WIDTH = 128
OLED_HEIGHT = 64

'''# Create a new blank canvas
canvas = Image.new('1', (OLED_WIDTH, OLED_HEIGHT), 255)
# Set up draw for the canvas
draw = ImageDraw.Draw(canvas)'''

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Buttons
#pinA = 4
pinA = 5
pinB = 6
pinC = 16
pinD = 24
pinE = 26

# buzzer
global pinnum
pinnum = 13

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


def buttonSetup():
  GPIO.setup(pinA, GPIO.IN)
  GPIO.setup(pinB, GPIO.IN)
  GPIO.setup(pinC, GPIO.IN)
  GPIO.setup(pinD, GPIO.IN)
  GPIO.setup(pinE, GPIO.IN)
  #GPIO.setup(pinF, GPIO.IN)

def buzzerSetup(pin):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  global pinnum
  pinnum = pin
  GPIO.setup(pinnum, GPIO.OUT) # This sets pin number from parameters as an output

def playFreqTime(freq, seconds):
  # This function plays a specified frequency for a specified time.
  # freq=0 is for a rest note.
  if freq == 0:
    #pwm_out = GPIO.PWM(pinnum, 1000)
    #pwm_out.stop()
    time.sleep(seconds)
  else:
    pwm_out = GPIO.PWM(pinnum, freq)
    pwm_out.start(50)
    time.sleep(seconds)
    pwm_out.stop()
    
def buzzUp3():
  playFreqTime(A5, .35)
  time.sleep(.2)
  playFreqTime(B5, .35)
  time.sleep(.2)
  playFreqTime(C6, .35)
  time.sleep(.1)
  
def buzzDown3():
  playFreqTime(C6, .35)
  time.sleep(.2)
  playFreqTime(B5, .35)
  time.sleep(.2)
  playFreqTime(A5, .35)
  time.sleep(.1)

def buzzUp2():
  playFreqTime(A5, .35)
  time.sleep(.2)
  playFreqTime(C6, .35)
  time.sleep(.1)
  
def buzzDown2():
  playFreqTime(C6, .35)
  time.sleep(.2)
  playFreqTime(A5, .35)
  time.sleep(.1)
  
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
#LED functions

#setup the pins as outputs and set the clocks initally to low and the clear initially to high. 
def setupLED():
  GPIO.setwarnings(False)
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
      hexLEDList.append(int(byte,2))
      byte = ""
    i+=1
  return hexLEDList[::-1]
      
'''This function allows you to turn on the lowest currently off led in the chain or turn off the highedst currently on led in the chain
Arguements: bool on or off and amount of leds you want to toggle'''
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
              
def getAvailable():
  return available_led

def resetAvailableLED():
  global available_led
  available_led = NUM_LEDS
  
'''This function turns on all LEDs'''
def allOn():

  for i in range(NUM_LEDS):
    ledList[i]=1
  print("IN ALL ON, disp List:", ledList)
  displayLED()
  


  
# Returns the state of button at given pin
def readButton(pin):
  return GPIO.input(pin)

def waitButton(pin):
  # print("Waiting for edge on pin", pin)
  GPIO.wait_for_edge(pin, GPIO.RISING, bouncetime=200)
  # print("Button pressed on pin", pin)
  # return

'''with canvas(device) as draw:
    draw.line((0, 45, 127 ,45), fill="white")
    draw.text((40, 43), "Welcome", fill="white")'''
