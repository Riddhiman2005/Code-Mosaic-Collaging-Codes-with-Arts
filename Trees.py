
import numpy as np
import matplotlib.pyplot as plt

def draw_tree(x, y, length, angle, depth):
    if depth > 0:
        x_end = x + length * np.sin(np.radians(angle))
        y_end = y + length * np.cos(np.radians(angle))

        plt.plot([x, x_end], [y, y_end], color='green', lw=2)

        draw_tree(x_end, y_end, length * 0.7, angle - 30, depth - 1)
        draw_tree(x_end, y_end, length * 0.7, angle + 30, depth - 1)

# Set up the plot

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Starting point and parameters
start_x = 0
start_y = 0
trunk_length = 1
trunk_angle = 90
tree_depth = 10

# Generate the tree
draw_tree(start_x, start_y, trunk_length, trunk_angle, tree_depth)

# Show the plot
plt.show()
