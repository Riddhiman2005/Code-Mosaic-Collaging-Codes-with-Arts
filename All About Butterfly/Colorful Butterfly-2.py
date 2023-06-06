
import numpy as np
import matplotlib.pyplot as plt

# Generating the butterfly shape plot

t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

# Create a color palette for the wings
# You can choose your own color

wing_colors = ['orange', 'yellow']

# Creating the plot

plt.figure(figsize=(8, 6))

# Plot the wings

plt.fill(x[:500], y[:500], color=wing_colors[0], alpha=0.8)
plt.fill(x[500:], y[500:], color=wing_colors[1], alpha=0.8)

# Setting plot properties

plt.axis('off')
plt.title('Butterfly', fontsize=16, fontweight='bold')
plt.tight_layout()

# Show plot

plt.show()

