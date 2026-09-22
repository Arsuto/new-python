import matplotlib.pyplot as plt
# Data for plotting
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b')
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
# Display the plot
plt.show()

#________________________________________________

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
# Create a figure and an axis
fig, ax = plt.subplots()
# Generate initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
# Create a line object that will be updated during the animation
line, = ax.plot(x, y)
# Function to update the plot for each frame
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0)) # Shift the sine wave
    return line,
# Create an animation object
ani = animation.FuncAnimation(fig, update , frames=100, interval=50, blit=True)

# Display the animation
plt.show()