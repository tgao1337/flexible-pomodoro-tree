import SSD1106
import time
from PIL import Image,ImageDraw,ImageFont

# Setup the display by creating an SH1106 object
display = SSD1106.SSD1106()
# Initialize it
display.setup()
# Create a new image
image = Image.new('1', (display.width, display.height), "WHITE")
draw = ImageDraw.Draw(image)
# Select default font and size
default_font = ImageFont.truetype('Font.ttf', 10)

def show():
    # Need to invert since display by default shows inverted image
    setup()
    img = invert(image) 
    display.ShowImage(display.getbuffer(img))

def setup():
    # Making a border
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)

    # Making a line
    draw.line([(0,12),(127,12)], fill = 0)

    # Text we want to display
    draw.text((6,0), 'Flexible Pomodoro Tree', font = default_font, fill = 0)

def clear():
    # Clear the display
    display.clear()
    draw.rectangle((0,0,128,64), outline=255, fill=255)
    #setup()

def write(text, x, y, size):
    # Setting up font
    font1 = ImageFont.truetype('Font.ttf', size)

    # Text we want to display
    draw.text((x,y), text, font = font1, fill = 0)
    #setup()

def invert(img):
     return img.rotate(180)

# Test code below

if __name__ == "__main__":
     show()
     time.sleep(2)

     clear()
     time.sleep(2)

     write("ECE-UY 4323", 30, 25, 10)
     write("CompE DP II", 30, 35, 10)
     show()
     time.sleep(2)

     clear()
     write("SSD1106", 35, 25, 15)
     show()
     time.sleep(2)
     clear()
     show()

