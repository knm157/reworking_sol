import matplotlib.pyplot as plt
import numpy as np
import os

def generate_unique_filename(base_name="wall_drawing_118", folder="drawings", extension="png"):
    """Generate an auto-incremented filename to prevent overwriting."""
    os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
    counter = 1
    while True:
        filename = f"{folder}/{base_name}_{counter:03d}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def save_high_res_drawing(dpi=600):
    """Save Wall Drawing #118 as a high-resolution PNG & SVG with user-defined points."""
    
    # Get user input for the number of points
    try:
        num_points = int(input("Enter the number of random points (default: 50): ") or 50)
    except ValueError:
        print("Invalid input. Using default value of 50.")
        num_points = 50

    # Generate unique filenames for PNG and SVG
    png_filename = generate_unique_filename(folder="drawings", extension="png")
    svg_filename = generate_unique_filename(folder="drawings/svg", extension="svg")

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8), dpi=dpi)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Generate random points
    points = np.random.rand(num_points, 2)

    # Draw connections between all points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], 
                    color="black", linewidth=0.5)

    # Save as high-resolution PNG
    plt.savefig(png_filename, dpi=dpi, bbox_inches='tight', format="png")

    # Save as SVG for vector output
    plt.savefig(svg_filename, bbox_inches='tight', format="svg")

    print(f"Drawing saved as: {png_filename}")
    print(f"SVG saved as: {svg_filename}")

# Run the function with user input
save_high_res_drawing()

