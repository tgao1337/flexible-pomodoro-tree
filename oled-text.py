import SSD1106
import time
from PIL import Image,ImageDraw,ImageFont

try:
    # Setup the display by creating an SH1106 object
    display = SSD1106.SSD1106()

    # Initialize the display
    display.setup()

    # Clear the display
    display.clear()

    # Then we create a new blank canvas
    image = Image.new("1", (display.width, display.height), "WHITE")
    draw = ImageDraw.Draw(image)

    # Setting up font
    font1 = ImageFont.truetype("Font.ttf", 10)
    font2 = ImageFont.truetype("Font.ttf",13)

    # Making a border on the canvas
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)

    # Text we want to display
    draw.text((6,0), "Flexible Pomodoro Tree", font = font1, fill = 0)
    draw.text((28,20), "CompE DP II", font = font2, fill = 0)

    image = image.rotate(180) # We rotate the image because otherwise its inverted on OLED
    
    # Call ShowImage to display on the OLED
    display.ShowImage(display.getbuffer(image))
    time.sleep(2)
    
#except IOError as e:
    #print(e)
    
except KeyboardInterrupt:    
    print("Interrupt occurred")
    #epdconfig.module_exit()
    config.module_exit()
    exit()
