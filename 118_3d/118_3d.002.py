import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

from mpl_toolkits.mplot3d import Axes3D

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
    """Generate, visualize, and save Wall Drawing #118 in 3D."""
    
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

    # Generate unique filenames
    point_filename = generate_unique_filename(extension="txt")
    fig_filename = generate_unique_filename(extension="fig.pickle")  # Save 3D plot

    # Generate random points in 3D space
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

    # Set limits based on cube size
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

    # Save the figure for later reloading
    with open(fig_filename, "wb") as f:
        pickle.dump(fig, f)

    print(f"3D Plot saved as: {fig_filename}")

    # Show the interactive plot
    plt.show()

def load_wall_drawing_118_3d():
    """Allow user to reload and view a saved 3D plot."""
    folder = "drawings_3d"
    files = sorted([f for f in os.listdir(folder) if f.endswith(".fig.pickle")])

    if not files:
        print("No saved 3D plots found!")
        return

    print("\nAvailable 3D Plots:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nEnter the number of the file to load: ")) - 1
        if choice < 0 or choice >= len(files):
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid input!")
        return

    # Load and display the selected figure
    fig_path = os.path.join(folder, files[choice])
    with open(fig_path, "rb") as f:
        fig = pickle.load(f)

    print(f"Loaded 3D Plot: {fig_path}")
    plt.show(fig)

# User selection menu
if __name__ == "__main__":
    print("\nOptions:")
    print("1. Generate a new 3D Wall Drawing #118")
    print("2. Load a previously saved 3D plot")
    
    choice = input("\nEnter your choice (1/2): ")
    
    if choice == "1":
        save_wall_drawing_118_3d()
    elif choice == "2":
        load_wall_drawing_118_3d()
    else:
        print("Invalid choice! Exiting.")

