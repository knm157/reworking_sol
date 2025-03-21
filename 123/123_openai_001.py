import numpy as np
import matplotlib.pyplot as plt

def draw_wall_drawing_123(
    num_lines=30, 
    height=100, 
    width=30, 
    noise_factor=5, 
    bg_color="white", 
    line_color="black"
):
    """Generate Sol LeWitt's Wall Drawing #123 using Matplotlib."""
    
    fig, ax = plt.subplots(figsize=(8, 10), dpi=300)
    ax.set_xlim(0, num_lines * width)
    ax.set_ylim(0, height)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.set_facecolor(bg_color)  # Set background color
    
    # Generate the first random line
    x = np.full(height, 0)  # Start at x=0
    y = np.arange(height)  # y goes from 0 to height-1
    x + np.cumsum(np.random.uniform(-noise_factor, noise_factor, height))
    
    # Store lines as we go
    lines = [x.copy()]

    # Copy the last drawn line with small variations
    for i in range(1, num_lines):
        new_x = lines[-1] + np.random.uniform(-noise_factor, noise_factor, height)
        lines.append(new_x)

    # Draw all lines
    for i, line in enumerate(lines):
        ax.plot(line + i * width, y, color=line_color, linewidth=1)

    plt.show()

# Generate LeWitt's Drawing #123
draw_wall_drawing_123()
