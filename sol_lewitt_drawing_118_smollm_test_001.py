import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define the dimensions of the drawing
x = 0
y = 0
width = 50
height = 40

# Create a new figure and axis
fig, ax = plt.subplots()

# Draw the rectangle with red fill color and no border
rect = Rectangle((x, y), width, height, facecolor='red', edgecolor='none')
ax.add_patch(rect)

# Set title of plot
plt.title("Sol LeWitt's Drawing #118")

# Set x and y limits to fit within the rectangle
ax.set_xlim(x-width/2, x+width/2 + width)
ax.set_ylim(y-height/2, y+height/2 + height)

# Save figure as an image file
plt.savefig('sol_lewitt_drawing_118_sml.png', bbox_inches='tight')
plt.savefig('sol_lewitt_drawing_118_600dpi.png', dpi=600, bbox_inches='tight')

