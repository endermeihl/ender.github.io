import numpy as np
from scipy.integrate import quad

def f(x):
    return np.exp(-x * x / 2) / np.sqrt(2 * np.pi)

integral, error = quad(f, -5, 5)
print(integral)