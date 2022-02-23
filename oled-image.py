import SH1106, config
from PIL import Image

# Initialise a display
display = SH1106.SH1106()
display.Init()
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

