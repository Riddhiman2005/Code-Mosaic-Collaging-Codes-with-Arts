
import numpy as np
import matplotlib.pyplot as plt

# Generate data points
t = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(t) + 0.5 * np.sin(10 * t)
y = np.cos(t) - 0.5 * np.cos(10 * t)

# Create a colormap for filling
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(x)))

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=2)
ax.fill_between(x, y, color=colors)

# Remove axes
ax.axis('off')

# Set plot properties
ax.set_title('Beautiful Design', fontsize=16)

# Display the plot
plt.show()
