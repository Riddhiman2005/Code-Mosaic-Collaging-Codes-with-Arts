
import matplotlib.pyplot as plt
import numpy as np

# Defining the x values
x = np.linspace(0, 180, 1000)

# Defining the y values for the rainbow curve
y = np.sin(np.radians(x))

# Defining the colors for the rainbow: VIBGYOR
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Creating the plot
plt.figure(figsize=(8, 6))

# Plotting the rainbow curve only for x between 0 and 180
# So from 0- 90 degree the curve will have increasing value and from
# 90 to 180 degree the curve will have decreasing values helping us to design our plot according to our expectations

mask = np.logical_and(x >= 0, x <= 180)
if np.any(mask):
    for i in range(len(rainbow_colors)):
        plt.fill_between(x[mask], i * np.sin(np.radians(x[mask])), (i + 1) * np.sin(np.radians(x[mask])), color=rainbow_colors[i])

# Set plot properties

plt.title('Rainbow Plot', fontsize=16, fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
