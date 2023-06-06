
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x_face = 4 * np.sin(t)
y_face = 4 * np.cos(t)

x_mouth = np.linspace(-1.5, 1.5, 100)
y_mouth = -0.8 * np.cos(x_mouth) - 2

plt.fill(x_face, y_face, color='yellow')
plt.plot(x_mouth, y_mouth, color='black', linewidth=3)

# Circular black eyes

eye_radius = 16
eye_y = 1.8

plt.scatter(-1.2, eye_y, color='black', s=100)  # Left eye
plt.scatter(1.2, eye_y, color='black', s=100)   # Right eye

plt.axis('equal')
plt.axis('off')
plt.xlim(-5, 5)
plt.ylim(-5, 5)


# Display The Plot

plt.show()
