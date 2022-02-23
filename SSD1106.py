import RPi.GPIO as GPIO
from smbus import SMBus
import time
import numpy as np

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
        self.write(0x02)	# Set low column address
        self.write(0x10)	# Set high column address
        self.write(0x40)	# Set start line address  Set Mapping RAM Display Start Line (0x00~0x3F)
        self.write(0x81)	# Set contrast control register
        self.write(0xA0)	# Set SEG/Column Mapping     
        self.write(0xC0)	# Set COM/Row Scan Direction   
        self.write(0xA6)	# Set normal display
        self.write(0xA8)	# Set multiplex ratio(1 to 64)
        self.write(0x3F)	# 1/64 duty
        self.write(0xD3)	# Set display offset    Shift Mapping RAM Counter (0x00~0x3F)
        self.write(0x00)	# Not offset
        self.write(0xd5)	# Set display clock divide ratio/oscillator frequency
        self.write(0x80)	# Set divide ratio, Set Clock as 100 Frames/Sec
        self.write(0xD9)	# Set pre-charge period
        self.write(0xF1)	# Set Pre-Charge as 15 Clocks & Discharge as 1 Clock
        self.write(0xDA)	# Set com pins hardware configuration
        self.write(0x12)
        self.write(0xDB)	# Set vcomh
        self.write(0x40)	# Set VCOM Deselect Level
        self.write(0x20)	# Set Page Addressing Mode (0x00/0x01/0x02)
        self.write(0x02)
        self.write(0xA4)	# Disable Entire Display On (0xa4/0xa5)
        self.write(0xA6)	# Disable Inverse Display On (0xa6/a7) 
        time.sleep(0.1)
        self.write(0xAF)	# Turn on oled panel


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
            # set page address #
            self.write(0xB0 + page);
            # set low column address #
            self.write(0x02); 
            # set high column address #
            self.write(0x10); 
            # write data #
            # time.sleep(0.01)
            for i in range(0,self.width):#for(int i=0;i<self.width; i++)
                #config.i2c_writebyte(0x40, ~pBuf[i+self.width*page])
                self.bus.write_byte_data(self.address, 0x40, ~pBuf[i+self.width*page])


    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff]*(self.width * self.height//8)
        self.ShowImage(_buffer)
