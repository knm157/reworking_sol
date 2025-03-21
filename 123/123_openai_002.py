import numpy as np
import matplotlib.pyplot as plt

def draw_wall_drawing_123(
    filename="123_002.png",
    num_lines=60, 
    plot_height_mm=1000, 
    plot_width_mm=700, 
    noise_factor=0.5, 
    dpi=600, 
    bg_color="white", 
    line_color="black"
):
    """Generate Sol LeWitt's Wall Drawing #123 and save as a high-resolution PNG."""
    
    # Convert mm to inches for Matplotlib
    mm_to_inch = 1 / 25.4
    fig, ax = plt.subplots(figsize=(plot_width_mm * mm_to_inch, plot_height_mm * mm_to_inch), dpi=dpi)
    
    # Set up the plot limits in mm
    ax.set_xlim(0, plot_width_mm)
    ax.set_ylim(0, plot_height_mm)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.set_facecolor(bg_color)  # Set background color
    
    # Scale factor for mm-based coordinates
    line_spacing = plot_width_mm / num_lines

    # Generate the first non-straight line
    x = np.full(plot_height_mm, 0)  # Start at x=0
    y = np.arange(plot_height_mm)  # y goes from 0 to height-1
    x + np.cumsum(np.random.uniform(-noise_factor, noise_factor, plot_height_mm))  # Add noise

    # Store lines as we go
    lines = [x.copy()]

    # Copy the last drawn line with small variations
    for i in range(1, num_lines):
        new_x = lines[-1] + np.random.uniform(-noise_factor, noise_factor, plot_height_mm)
        lines.append(new_x)

    # Draw all lines
    for i, line in enumerate(lines):
        ax.plot(line + i * line_spacing, y, color=line_color, linewidth=0.5)

    # Save as high-quality PNG
    plt.savefig(filename, dpi=dpi, bbox_inches='tight', format="png")
    print(f"Drawing saved as: {filename}")

# Generate LeWitt's Drawing #123 with custom mm settings
draw_wall_drawing_123(
    filename="wall_drawing_123_highres.png",
    plot_height_mm=1000,  # Set height in mm
    plot_width_mm=700,    # Set width in mm
    dpi=600               # High resolution for printing
)
