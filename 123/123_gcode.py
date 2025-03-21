def generate_gcode_123(
    filename="wall_drawing_123.gcode",
    num_lines=30, 
    height=1000, 
    width=30, 
    noise_factor=10, 
    scale=1
):
    """Generate G-code for CNC drawing of Sol LeWitt's Wall Drawing #123."""
    
    with open(filename, "w") as f:
        f.write("; G-code for Sol LeWitt's Wall Drawing #123\n")
        f.write("G21 ; Set units to mm\n")
        f.write("G90 ; Absolute positioning\n")
        f.write("G0 Z5 ; Lift pen up\n")

        # Generate the first non-straight line
        x = np.full(height, 0)  # Start at x=0
        y = np.arange(height) * scale  # Scale for CNC (millimeters)
        x += np.cumsum(np.random.uniform(-noise_factor, noise_factor, height)) * scale

        # Store lines
        lines = [x.copy()]

        # Copy the last drawn line with small variations
        for i in range(1, num_lines):
            new_x = lines[-1] + np.random.uniform(-noise_factor, noise_factor, height) * scale
            lines.append(new_x)

        # Convert to G-code commands
        for i, line in enumerate(lines):
            x_offset = i * width * scale  # Offset for each new line
            f.write(f"G0 X{x_offset:.2f} Y{y[0]:.2f} ; Move to start\n")
            f.write("M3 S100 ; Pen down\n")  # Start drawing

            for j in range(1, height):
                f.write(f"G1 X{line[j] + x_offset:.2f} Y{y[j]:.2f} F3000\n")

            f.write("M5 ; Pen up\n")  # Lift pen after line

        f.write("G0 Z5 ; Lift pen at end\n")
        f.write("G0 X0 Y0 ; Return to home\n")
        f.write("M2 ; End of program\n")

    print(f"G-code saved as: {filename}")

# Generate G-code for a CNC version of Drawing #123
generate_gcode_123("wall_drawing_123.gcode")

