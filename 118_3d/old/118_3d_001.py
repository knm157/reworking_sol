import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def generate_unique_filename(base_name="wall_drawing_118_3d", folder="drawings_3d", extension="txt"):
    """Generate an auto-incremented filename to prevent overwriting."""
    os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
    counter = 1
    while True:
        filename = f"{folder}/{base_name}_{counter:03d}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def save_wall_drawing_118_3d():
    """Generate and visualize Wall Drawing #118 in 3D with interactive exploration."""
    
    # User input for 3D cube size (in meters)
    try:
        cube_size = float(input("Enter the 3D plot size in meters (default: 1m): ") or 1.0)
    except ValueError:
        print("Invalid input. Using default value of 1m.")
        cube_size = 1.0

    # User input for number of points
    try:
        num_points = int(input("Enter the number of random points (default: 50): ") or 50)
    except ValueError:
        print("Invalid input. Using default value of 50.")
        num_points = 50

    # Generate unique filename for saving points
    point_filename = generate_unique_filename()

    # Generate random points in a 3D space within the defined cube size
    points = np.random.rand(num_points, 3) * cube_size  # Scale points to fit cube_size³

    # Save the 3D points to a file
    with open(point_filename, "w") as f:
        f.write("X,Y,Z\n")
        for p in points:
            f.write(f"{p[0]:.4f},{p[1]:.4f},{p[2]:.4f}\n")

    print(f"3D Points saved as: {point_filename}")

    # Create a 3D figure
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Set limits based on user-defined cube size
    ax.set_xlim(0, cube_size)
    ax.set_ylim(0, cube_size)
    ax.set_zlim(0, cube_size)

    ax.set_xlabel("X Axis (m)")
    ax.set_ylabel("Y Axis (m)")
    ax.set_zlabel("Z Axis (m)")
    ax.set_title(f"Wall Drawing #118 - 3D Visualization ({cube_size}m³)")

    # Connect every point to every other point
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ax.plot([points[i][0], points[j][0]], 
                    [points[i][1], points[j][1]], 
                    [points[i][2], points[j][2]], 
                    color="black", linewidth=0.5)

    # Enable interactive rotation with mouse
    plt.show()

# Run the function
if __name__ == "__main__":
    save_wall_drawing_118_3d()

