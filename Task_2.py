import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(x, y, angle, length, depth):
    if depth == 0:
        return

    # Calculate the end point of the current line
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Draw the current line
    plt.plot([x, x_end], [y, y_end], color='green')

    # Calculate the next branch length (shorter)
    new_length = length * 0.7

    # Branch angles: 45° up-left and 45° up-right from the current direction
    left_angle = angle + np.pi / 4
    right_angle = angle - np.pi / 4

    # Recursively draw two new branches
    draw_pythagoras_tree(x_end, y_end, left_angle, new_length, depth - 1)
    draw_pythagoras_tree(x_end, y_end, right_angle, new_length, depth - 1)

# --- Main section ---
if __name__ == "__main__":
    depth = int(input("Enter recursion depth (e.g., 10): "))

    plt.figure(figsize=(10, 10))
    plt.axis('equal')
    plt.axis('off')

    # Starting coordinates 
    start_x, start_y = 0, 0
    initial_length = 100
    initial_angle = np.pi / 2  # 90° — straight up

    # Start the recursion
    draw_pythagoras_tree(start_x, start_y, initial_angle, initial_length, depth)

    plt.title("Pythagoras Tree Fractal")
    plt.show()
