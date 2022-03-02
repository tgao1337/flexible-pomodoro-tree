# This will be the foo.py in the example slides Professor Fund showed.
import pigpio
import time

from smbus import SMBus
from PIL import Image,ImageDraw,ImageFont

OLED_WIDTH = 128
OLED_HEIGHT = 64

# Create a new blank canvas
canvas = Image.new('1', (OLED_WIDTH, OLED_HEIGHT), 255)
# Set up draw for the canvas
draw = ImageDraw.Draw(canvas)

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
