import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = np.exp(-x * x / 2) / np.sqrt(2 * np.pi)

plt.plot(x, y)
plt.show()