import matplotlib.pyplot as plt
import numpy as np

def save_high_res_drawing(filename="wall_drawing_118.png", dpi=600, points=None):
    """Save Wall Drawing #118 as a high-resolution image."""
    
    fig, ax = plt.subplots(figsize=(8, 8), dpi=dpi)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    if points is None:
        num_points = 50
        points = np.random.rand(num_points, 2)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], 
                    color="black", linewidth=0.5)

    plt.savefig(filename, dpi=dpi, bbox_inches='tight', format="png")
    print(f"Drawing saved as: {filename}")

# Save as a 600 DPI high-res PNG
save_high_res_drawing("wall_drawing_high_res.png", dpi=600)
