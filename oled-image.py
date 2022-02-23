import SSD1106
from PIL import Image

# Initialise a display
display = SSD1106.SSD1106()
display.setup()
display.clear()

# Creating a blank canvas
image = Image.new('1', (128, 64), 255)
# Open the image you want to display
clown = Image.open("clown.bmp")
# Paste the image on existing canvas with coordinates 
image.paste(clown, (40,0)) # (40,0) will center align this image
# Rotate image
image = image.rotate(180)
display.ShowImage(display.getbuffer(image))

