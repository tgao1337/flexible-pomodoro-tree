import RPi.GPIO as GPIO
from smbus import SMBus
import time

OLED_WIDTH = 128
OLED_HEIGHT = 64

class SSD1106(object):
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
        _buffer = [0xff]*(self.width * self.height//8)
        self.ShowImage(_buffer)
