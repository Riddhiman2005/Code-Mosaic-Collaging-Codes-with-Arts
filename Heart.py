

import numpy as np
import matplotlib.pyplot as plt

# Generate the heart shape curve
t = np.linspace(0, 2*np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='red', linewidth=2)
plt.fill(x, y, 'red')

# Set plot properties
plt.axis('off')
plt.title('Love Heart', fontsize=16, fontweight='bold')
plt.tight_layout()

# Display the plot
plt.show()
