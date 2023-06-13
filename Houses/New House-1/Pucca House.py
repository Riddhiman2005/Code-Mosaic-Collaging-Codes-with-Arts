
# Two Floored Pucca House

import matplotlib.pyplot as plt

# Creating the figure and axes
fig, ax = plt.subplots()

# Walls for the Ground floor
ax.add_patch(plt.Rectangle((0, 0), 6, 4, color='yellow'))

# Walls for the First floor
ax.add_patch(plt.Rectangle((0, 4), 6, 4, color='orange'))

# Roof for the Ground floor
ax.add_patch(plt.Rectangle((0, 8), 6, 0.5, color='green'))

# Roof for the First floor
ax.add_patch(plt.Rectangle((0, 3.5), 6, 0.5, color='green'))

# Door
ax.add_patch(plt.Rectangle((2.5, 0), 1, 2, color='brown'))

# Windows for the Ground floor
ax.add_patch(plt.Rectangle((0.8, 1.5), 1, 1, color='blue'))
ax.add_patch(plt.Rectangle((4, 1.5), 1, 1, color='blue'))

# Windows for the First floor
ax.add_patch(plt.Rectangle((0.8, 5.5), 1, 1, color='skyblue'))
ax.add_patch(plt.Rectangle((4, 5.5), 1, 1, color='skyblue'))



# Set plot limits
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 10)

# Remove labels
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Show the plot
plt.show()
