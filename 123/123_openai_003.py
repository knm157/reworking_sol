import numpy as np
import matplotlib.pyplot as plt
import os

def generate_unique_filename(base_name, folder=".", extension="png"):
    """Check for existing files and auto-increment the filename."""
    counter = 1
    while True:
        filename = f"{folder}/{base_name}_{counter:03d}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def draw_wall_drawing_123(
    num_lines=75, 
    plot_height_mm=430, # Epson 5070 default output, fixed width of paper roll.
    plot_width_mm=430, # Make it square, I am printing it width as roll length 
    noise_factor=0.5, 
    dpi=600, 
    bg_color="white", 
    line_color="black", 
    save_folder="drawings"
):
    """Generate Sol LeWitt's Wall Drawing #123 and save as a high-resolution PNG with unique names."""

    # Ensure the save folder exists
    os.makedirs(save_folder, exist_ok=True)

    # Generate a unique filename based on parameters
    base_filename = f"wall_drawing_123_{num_lines}lines_{plot_height_mm}mm_{plot_width_mm}mm_{noise_factor}noise_{bg_color}BG_{line_color}FG"
    save_path = generate_unique_filename(base_filename, folder=save_folder, extension="png")

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
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight', format="png")
    print(f"Drawing saved as: {save_path}")

# Generate LeWitt's Drawing #123 with auto-incremented filenames
draw_wall_drawing_123(
    num_lines=75, 
    plot_height_mm=430, # Epson 5070 default output, fixed width of paper roll.
    plot_width_mm=430, # Make it square, I am printing it width as roll length 
    noise_factor=0.5, 
    dpi=600, 
    bg_color="white", 
    line_color="black"
)

