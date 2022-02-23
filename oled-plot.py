import matplotlib.pyplot as plt
import SSD1106
from PIL import Image
import numpy as np

display = SSD1106.SSD1106()
display.setup()
display.clear()

# Creatinng a plot figure of size 1.3x0.9 inches (OLED display size)
fig = plt.figure(figsize=(1.3, 0.9), dpi=98)
ax = fig.add_axes((0.15, 0.25, 0.8, 0.7))

# ===== PLOT 1
'''
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

ax.plot(x, y, linewidth=1.0)

ax.set(xlim=(0, 8), xticks=np.arange(0, 9, 4),
       ylim=(0, 8), yticks=np.arange(0, 9, 4))
'''
# ===== END OF PLOT 1

# ===== PLOT 2

ax.plot([1,2,3], [2,4,8])
ax.set(xlim=(0, 4), xticks=np.arange(0, 9, 1),
       ylim=(0, 8), yticks=np.arange(0, 9, 4))

# ===== END OF PLOT 2


# ===== BAR GRAPH
'''
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(0, 9, 4),
       ylim=(0, 8), yticks=np.arange(0, 9, 4))
'''
# ===== END OF BAR GRAPH



# Saving plot
plt.savefig("plot.png", format="png")


# Creating a blank canvas
image = Image.new('1', (128,64), 255)

# Open the plot
plot = Image.open("plot.png").resize((128,64), Image.LANCZOS)
# Paste plot on existing canvas

image.paste(plot)

image = image.rotate(180)

display.ShowImage(display.getbuffer(image))

