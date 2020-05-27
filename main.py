import matplotlib.pyplot as plt
import numpy as np
from random import uniform 


# bounds of rng
lower = 0.25
upper = 1.0

x = np.arange(0.0, 1 * np.pi, 0.01)

for j in range(5):
    # random numbers
    r1 = uniform(lower, upper)
    r2 = uniform(lower, upper)
    r3 = uniform(lower, upper)
    r4 = uniform(lower, upper)

    # x = r1 * np.sin(2 * np.pi * r2 * x)
    # x = r3 * np.cos(2 * np.pi * r4 * x)

    y1 = r1 * np.sin(2 * np.pi * r2 * x)
    y2 = r3 * np.sin(2 * np.pi * r4 * x)

    # y1 = np.arange(0.0, 1 * np.pi, 0.01)
    # y2 = np.arange(0.0, 1 * np.pi, 0.01)

    cl = (uniform(0,1), uniform(0,1), uniform(0,1))
    plt.fill_between(x, y1, y2, color=cl)

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
ax.set_facecolor((uniform(0,1), uniform(0,1), uniform(0,1)))
plt.show()

