import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # End point of the current branch
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Draw the current branch
    plt.plot([x, x_end], [y, y_end], color='green')

    # Calculate the length for the next level (shorter)
    new_length = length * 0.7  # scaling factor

    # Recursively draw two branches from the end
    left_angle = angle + np.pi / 4   # 45° left
    right_angle = angle - np.pi / 4  # 45° right

    draw_branch(x_end, y_end, left_angle, new_length, depth - 1)
    draw_branch(x_end, y_end, right_angle, new_length, depth - 1)

# User input for recursion depth
depth = int(input("Enter recursion depth (e.g., 8): "))

# Set up the drawing canvas
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.axis('equal')

# Start with a horizontal base line, then draw two branching lines
start_x, start_y = 0, 0
initial_length = 100
initial_angle = 0  # horizontal line to the right

# Draw the base line manually
x_base_end = start_x + initial_length * np.cos(initial_angle)
y_base_end = start_y + initial_length * np.sin(initial_angle)
plt.plot([start_x, x_base_end], [start_y, y_base_end], color='brown')

# Start recursion from end of the base line
draw_branch(x_base_end, y_base_end, np.pi / 4, initial_length * 0.7, depth - 1)   # Left branch
draw_branch(x_base_end, y_base_end, -np.pi / 4, initial_length * 0.7, depth - 1)  # Right branch

# Display the tree
plt.show()
