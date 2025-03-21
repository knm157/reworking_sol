import matplotlib.pyplot as plt
import numpy as np

def get_user_input(prompt, default):
    """Helper function to get user input with a default value."""
    user_input = input(f"{prompt} (Default: {default}): ").strip()
    return user_input if user_input else default

def draw_wall_drawing_49():
    """Generate Sol LeWitt's Wall Drawing #49 with customizable colors and sizes."""

    # User input for colors
    colors = {
        "black": get_user_input("Enter color for black pencil lines", "black"),
        "yellow": get_user_input("Enter color for yellow lines", "yellow"),
        "red": get_user_input("Enter color for red lines", "red"),
        "blue": get_user_input("Enter color for blue lines", "blue")
    }

    # User input for wall dimensions
    width_mm = int(get_user_input("Enter wall width in mm", 1000))
    height_mm = int(get_user_input("Enter wall height in mm", 500))

    # Convert mm to inches for Matplotlib
    mm_to_inch = 1 / 25.4
    fig, ax = plt.subplots(figsize=(width_mm * mm_to_inch, height_mm * mm_to_inch), dpi=300)

    # Number of sections
    num_sections = 15
    section_width = width_mm / num_sections

    # Define line patterns
    patterns = {
        1: ["black"],         # Black vertical lines
        2: ["yellow"],        # Yellow horizontal lines
        3: ["red"],           # Red diagonal (↗)
        4: ["blue"],          # Blue diagonal (↘)
        5: ["black", "yellow"],
        6: ["black", "red"],
        7: ["black", "blue"],
        8: ["yellow", "red"],
        9: ["yellow", "blue"],
        10: ["red", "blue"],
        11: ["black", "yellow", "red"],
        12: ["black", "yellow", "blue"],
        13: ["black", "red", "blue"],
        14: ["yellow", "red", "blue"],
        15: ["black", "yellow", "red", "blue"]
    }

    # Generate the wall drawing
    for i in range(num_sections):
        x_start = (i / num_sections) * width_mm
        x_end = ((i + 1) / num_sections) * width_mm
        section_color = patterns[i + 1]

        for color in section_color:
            if color == "black":
                for x in np.linspace(x_start, x_end, 20):  # Vertical lines
                    ax.plot([x, x], [0, height_mm], color=colors[color], linewidth=1)
            
            if color == "yellow":
                for y in np.linspace(0, height_mm, 20):  # Horizontal lines
                    ax.plot([x_start, x_end], [y, y], color=colors[color], linewidth=1)
            
            if color == "red":
                for x in np.linspace(x_start, x_end, 20):  # Diagonal ↗
                    ax.plot([x, x + section_width], [0, height_mm], color=colors[color], linewidth=1)

            if color == "blue":
                for x in np.linspace(x_start, x_end, 20):  # Diagonal ↘
                    ax.plot([x, x + section_width], [height_mm, 0], color=colors[color], linewidth=1)

    # Formatting
    ax.set_xlim(0, width_mm)
    ax.set_ylim(0, height_mm)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Save and show
    plt.savefig("wall_drawing_49.png", dpi=300, bbox_inches="tight", format="png")
    plt.show()

# Run the function
draw_wall_drawing_49()

