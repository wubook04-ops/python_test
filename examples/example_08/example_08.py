import numpy as np
from scipy.optimize import fmin
def f(x):
    return x**2 + 10 * np.sin(x) + 1

min1 = fmin(f, 3)
min2 = fmin(f, 0)
print(min1)
print(min2)