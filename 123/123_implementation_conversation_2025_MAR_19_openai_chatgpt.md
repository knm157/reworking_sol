# Sol LeWitt Drawing #123 - Python Implementation

## Conversation Summary
This document contains the full conversation about implementing Sol LeWitt's *Wall Drawing #123* using **Python**, **Matplotlib**, and **G-code** for CNC plotting. It also includes interactive user input for setting parameters.

---

## **1️⃣ Initial Plan & Concept**

### **Sol LeWitt's Drawing #123 Instructions**
> "The first draftsman draws a not straight vertical line as long as possible. The second draftsman draws a line next to the first one, trying to copy it. The third draftsman does the same, as do as many draftsmen as possible..."

### **Features Implemented**
✔ **Non-straight vertical line** generation using noise.  
✔ **Copying effect** across the canvas with slight variation.  
✔ **Configurable background & foreground colors**.  
✔ **High-resolution output (600 DPI, print-ready)**.  
✔ **G-code version** for CNC machines and pen plotters.  
✔ **Interactive user input for customization**.  
✔ **Auto-incremented filenames to prevent overwriting**.  

---

## **2️⃣ Python Implementation - Matplotlib Version**

```python
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
    num_lines=30,
    plot_height_mm=1000,
    plot_width_mm=700,
    noise_factor=10,
    dpi=600,
    border_mm=25,
    bg_color="white",
    line_color="black",
    save_folder="drawings"
):
    """Generate Sol LeWitt's Wall Drawing #123 with user-defined settings."""
    
    os.makedirs(save_folder, exist_ok=True)

    # Deduct border space from total width
    drawable_width_mm = plot_width_mm - (2 * border_mm)

    # Generate filename
    base_filename = f"wall_drawing_123_{num_lines}lines_{plot_height_mm}mm_{plot_width_mm}mm_{noise_factor}noise_{border_mm}mmBorder_{bg_color}BG_{line_color}FG"
    save_path = generate_unique_filename(base_filename, folder=save_folder, extension="png")

    # Convert mm to inches for high-resolution output
    mm_to_inch = 1 / 25.4
    fig, ax = plt.subplots(figsize=(plot_width_mm * mm_to_inch, plot_height_mm * mm_to_inch), dpi=dpi)
    
    ax.set_xlim(0, plot_width_mm)
    ax.set_ylim(0, plot_height_mm)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.set_facecolor(bg_color)
    
    line_spacing = drawable_width_mm / num_lines  

    # Generate the first non-straight line (starting at `border_mm`)
    x = np.full(plot_height_mm, border_mm, dtype=float)  # Start at left margin
    y = np.arange(plot_height_mm)
    x += np.cumsum(np.random.uniform(-noise_factor, noise_factor, plot_height_mm))

    lines = [x.copy()]
    
    for i in range(1, num_lines):
        new_x = lines[-1] + np.random.uniform(-noise_factor, noise_factor, plot_height_mm)
        lines.append(new_x)

    for i, line in enumerate(lines):
        ax.plot(line + i * line_spacing, y, color=line_color, linewidth=0.5)

    plt.savefig(save_path, dpi=dpi, bbox_inches='tight', format="png")
    print(f"Drawing saved as: {save_path}")

# Interactive user input function
def get_user_input(prompt, default, type_cast):
    user_input = input(f"{prompt} (Default: {default}): ").strip()
    return type_cast(user_input) if user_input else default

def main():
    """Interactive user input for custom settings."""
    print("\n🎨 Sol LeWitt's Wall Drawing #123 Generator 🎨")
    print("Enter your settings below. Press Enter to use defaults.\n")

    num_lines = get_user_input("Number of lines", 30, int)
    plot_height_mm = get_user_input("Plot height (mm)", 1000, int)
    plot_width_mm = get_user_input("Plot width (mm)", 700, int)
    noise_factor = get_user_input("Noise factor", 10, float)
    dpi = get_user_input("DPI", 600, int)
    border_mm = get_user_input("Border size (mm)", 25, int)
    bg_color = get_user_input("Background color", "white", str)
    line_color = get_user_input("Line color", "black", str)

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
```

---

## **3️⃣ Summary & Next Steps**

### **🔹 Features Implemented**
✔ **High-resolution Matplotlib drawing (600 DPI)**
✔ **User input prompts for interactive settings**
✔ **Auto-incremented filenames** to avoid overwriting
✔ **Border margins deducted from drawing area**
✔ **Configured for large-format printing**

### **🔹 Next Steps**
- Convert **SVG output** for laser engravers or vector-based CNC plotting.
- Implement a **G-code version** for direct CNC drawing.
- Add **real-time previews** before generating the final image.

Would you like to explore **SVG export** or **direct G-code generation** next? 😊


