#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot
plt.plot(x, y1, "-g", label="sine")
plt.plot(x, y2, "-b", label="cos")

# The legend should be in the top right corner
plt.legend(loc="upper right")

# Limit the y axis to -1.5-1.5 & x axis to 0-10
plt.ylim(-1.5, 1.5)
plt.xlim(0, 10)
plt.show()
