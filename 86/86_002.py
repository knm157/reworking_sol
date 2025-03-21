import numpy as np
import matplotlib.pyplot as plt
import os
import svgwrite
import time

def generate_unique_filename(base_name="86", folder="drawings", extension="png", height=2, width=5, num_lines=10000):
    """Generate an auto-incremented filename with user-defined settings."""
    os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
    counter = 1
    while True:
        filename = f"{folder}/{base_name}_{counter:03d}_{height}m_{width}m_{num_lines}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def draw_wall_drawing_86():
    """Generate Sol LeWitt's Wall Drawing #86 with user-defined settings."""
    
    # User input for dimensions, number of lines, and line length
    try:
        height_m = float(input("Enter the plot height in meters (default: 2m): ") or 2.0)
        width_m = float(input("Enter the plot width in meters (default: 5m): ") or 5.0)
        num_lines = int(input("Enter the number of random lines (default: 10000): ") or 10000)
        line_length_mm = float(input("Enter line length in mm (default: 254mm): ") or 254.0)
    except ValueError:
        print("Invalid input. Using default values.")
        height_m, width_m, num_lines, line_length_mm = 2.0, 5.0, 10000, 254.0

    # Convert meters to millimeters for SVG
    width_mm = width_m * 1000
    height_mm = height_m * 1000

    # Convert line length to meters
    line_length_m = line_length_mm / 1000.0

    # Generate unique filenames
    png_filename = generate_unique_filename(folder="drawings", extension="png", height=height_m, width=width_m, num_lines=num_lines)
    svg_filename = generate_unique_filename(folder="svg", extension="svg", height=height_m, width=width_m, num_lines=num_lines)
    txt_filename = generate_unique_filename(folder="points", extension="txt", height=height_m, width=width_m, num_lines=num_lines)

    # Create figure for Matplotlib
    fig, ax = plt.subplots(figsize=(width_m * 3, height_m * 3), dpi=300)
    ax.set_xlim(0, width_m)
    ax.set_ylim(0, height_m)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Initialize SVG file (convert meters to mm)
    os.makedirs("svg", exist_ok=True)
    dwg = svgwrite.Drawing(svg_filename, size=(f"{width_mm}mm", f"{height_mm}mm"))

    # Initialize text file
    os.makedirs("points", exist_ok=True)
    with open(txt_filename, "w") as f:
        f.write(f"####\n")
        f.write(f"# Wall Drawing matplotlib {png_filename}\n")
        f.write(f"#\n")
        f.write(f"# User input was Height(m): {height_m}, Width(m): {width_m}, Number of lines: {num_lines}\n")
        f.write(f"#\n#\n")
        f.write("x, y, degrees\n")

        # Generate and plot random lines
        for i in range(num_lines):
            # Random start point
            x_start = np.random.uniform(0, width_m)
            y_start = np.random.uniform(0, height_m)

            # Random angle (0-360 degrees)
            angle = np.random.uniform(0, 360)
            radians = np.radians(angle)

            # Compute end point
            x_end = x_start + np.cos(radians) * line_length_m
            y_end = y_start + np.sin(radians) * line_length_m

            # Draw in Matplotlib
            ax.plot([x_start, x_end], [y_start, y_end], color="black", linewidth=0.5)

            # Draw in SVG (scale to mm)
            dwg.add(dwg.line(start=(x_start * 1000, y_start * 1000), 
                             end=(x_end * 1000, y_end * 1000), 
                             stroke="black", stroke_width=0.5))

            # Save to text file
            f.write(f"{x_start:.4f}, {y_start:.4f}, {angle:.2f}\n")

            # Animate plotting process (optional)
            if i % 100 == 0:  # Update every 100 lines for efficiency
                plt.pause(0.001)

    # Save outputs
    plt.savefig(png_filename, dpi=300, bbox_inches="tight", format="png")
    dwg.save()

    print(f"Drawing saved as: {png_filename}")
    print(f"SVG saved as: {svg_filename}")
    print(f"Point data saved as: {txt_filename}")

    # Show plot (animated effect)
    plt.show()

# Run the function
draw_wall_drawing_86()

