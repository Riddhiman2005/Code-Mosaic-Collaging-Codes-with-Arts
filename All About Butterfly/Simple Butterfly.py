

import numpy as np
import matplotlib.pyplot as plt

# Generating the butterfly shape 
t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

# Creating the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', linewidth=2)

# Setting up the plot properties
plt.axis('off')
plt.title('Butterfly', fontsize=16, fontweight='bold')
plt.tight_layout()

# Show plot

plt.show()
