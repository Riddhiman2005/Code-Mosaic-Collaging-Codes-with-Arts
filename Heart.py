# Plotting Heart (love) in Python

import numpy as np
import matplotlib.pyplot as plt

# Generating the Love curve

t = np.linspace(0, 2*np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Creating the plot

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='red', linewidth=2)  # Red Color
plt.fill(x, y, 'red')                     # Filling the Curve with Red
 
# Plot properties

plt.axis('off')
plt.title('Love Heart', fontsize=16, fontweight='bold')
plt.tight_layout()

# Show plot

plt.show()
