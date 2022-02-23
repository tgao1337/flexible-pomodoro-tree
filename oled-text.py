import SSD1106
from PIL import Image,ImageDraw,ImageFont

# Setup the display by creating an SSD1106 object
display = SSD1106.SSD1106()
# Initialize the display
display.setup()
# Clear the display
display.clear()

# Create a new blank canvas
canvas = Image.new("1", (display.width, display.height), 255)
# Setup draw for the canvas
draw = ImageDraw.Draw(canvas)

# Setting up font
# Load default font
#font1 = ImageFont.load_default()
# Or load custom font with custom size
font1 = ImageFont.truetype("Font.ttf", 10)
font2 = ImageFont.truetype("Font.ttf",13)

# Making a border on the canvas
draw.line([(0,0),(127,0)])
draw.line([(0,0),(0,63)])
draw.line([(0,63),(127,63)])
draw.line([(127,0),(127,63)])

# Draw text on canvas
draw.text((6,0), "Flexible Pomodoro Tree", font = font1)
draw.text((28,20), "CompE DP II", font = font2)

# Rotate the canvas based on your OLED's orienntation
canvas = canvas.rotate(180)
# Call ShowImage to display canvas on the OLED
display.ShowImage(display.getbuffer(canvas))
