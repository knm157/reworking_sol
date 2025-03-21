import matplotlib.pyplot as plt
import numpy as np

# Set figure size and background
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)  # Remove borders for a clean look

# Generate 50 random points
num_points = 50
points = np.random.rand(num_points, 2)  # 50 (x, y) pairs

# Draw lines connecting every point to every other point
for i in range(num_points):
    for j in range(i + 1, num_points):  # Avoid duplicate connections
        ax.plot([points[i, 0], points[j, 0]], [points[i, 1], points[j, 1]], 
                color="black", linewidth=0.5)

# Show the artwork
plt.show()

