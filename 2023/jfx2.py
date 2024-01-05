import numpy as np
from scipy.integrate import quad

def f(x):
    return x*x

integral, error = quad(f, 0, 1)
print(integral)