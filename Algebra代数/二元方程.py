from matplotlib import pyplot
import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return math.pow(x, 2)
    
x = np.arange(-10, 10, dtype=np.int16)
print(x)

y = [f(i) for i in x]
print(y)

plt.plot(x, y)
plt.show()