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
    plot_width_mm=430,  # Make it square, I am printing it width as roll length
    noise_factor=0.25, 
    dpi=600, 
    border_mm=25, 
    bg_color="white", 
    line_color="black", 
    save_folder="drawings"
):
    """Generate Sol LeWitt's Wall Drawing #123 with user-defined settings."""
    
    # Ensure the save folder exists
    os.makedirs(save_folder, exist_ok=True)

    # Calculate the drawable area (subtract borders)
    drawable_width_mm = plot_width_mm - (2 * border_mm)

    # Generate a unique filename
    base_filename = f"wall_drawing_123_{num_lines}lines_{plot_height_mm}mm_{plot_width_mm}mm_{noise_factor}noise_{border_mm}mmBorder_{bg_color}BG_{line_color}FG"
    save_path = generate_unique_filename(base_filename, folder=save_folder, extension="png")

    # Convert mm to inches for Matplotlib
    mm_to_inch = 1 / 25.4
    fig, ax = plt.subplots(figsize=(plot_width_mm * mm_to_inch, plot_height_mm * mm_to_inch), dpi=dpi)

    # Set up the plot limits
    ax.set_xlim(0, plot_width_mm)
    ax.set_ylim(0, plot_height_mm)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.set_facecolor(bg_color)  # Set background color
    
    # Scale factor for mm-based coordinates
    line_spacing = drawable_width_mm / num_lines  

    # Generate the first non-straight line (starting at `border_mm`)
    x = np.full(plot_height_mm, border_mm, dtype=float)  # Start at left margin
    y = np.arange(plot_height_mm)  # y goes from 0 to height-1
    x += np.cumsum(np.random.uniform(-noise_factor, noise_factor, plot_height_mm))  # Add noise

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

# 🔹 Interactive User Input
def get_user_input(prompt, default, type_cast):
    """Helper function to get user input with a default value."""
    user_input = input(f"{prompt} (Default: {default}): ").strip()
    return type_cast(user_input) if user_input else default

def main():
    """Interactive script to get user input and generate a drawing."""
    
    print("\n Sol LeWitt's Wall Drawing #123 Generator ")
    print("Enter your settings below. Press Enter to use defaults.\n")

    num_lines = get_user_input("Number of lines", 75, int)
    plot_height_mm = get_user_input("Plot height (mm)", 430, int)
    plot_width_mm = get_user_input("Plot width (mm)", 430, int)
    noise_factor = get_user_input("Noise factor (line waviness) try under 1", 0.25, float)
    dpi = get_user_input("DPI (image resolution)", 600, int)
    border_mm = get_user_input("Border size (mm)", 25, int)
    bg_color = get_user_input("Background color (white/black)", "white", str)
    line_color = get_user_input("Line color (black/white)", "black", str)

    # Generate the drawing with user-defined settings
    draw_wall_drawing_123(
        num_lines=num_lines,
        plot_height_mm=plot_height_mm,
        plot_width_mm=plot_width_mm,
        noise_factor=noise_factor,
        dpi=dpi,
        border_mm=border_mm,
        bg_color=bg_color,
        line_color=line_color
    )

if __name__ == "__main__":
    main()
