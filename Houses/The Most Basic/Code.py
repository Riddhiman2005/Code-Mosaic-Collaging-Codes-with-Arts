
import matplotlib.pyplot as plt

# Create the figure and axes
fig, ax = plt.subplots()

# Draw the walls
ax.add_patch(plt.Rectangle((0, 0), 6, 4, color='yellow'))

# Draw the roof
roof_points = [(0, 4), (3, 7), (6, 4)]
ax.add_patch(plt.Polygon(roof_points, color='red'))

# Draw the door
ax.add_patch(plt.Rectangle((2.5, 0), 1, 2, color='brown'))

# Draw the windows
ax.add_patch(plt.Rectangle((0.8, 1.5), 1.5, 1.5, color='skyblue'))
ax.add_patch(plt.Rectangle((3.8, 1.5), 1.5, 1.5, color='skyblue'))

# Set plot limits
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 8)

# Remove ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Show the plot
plt.show()
