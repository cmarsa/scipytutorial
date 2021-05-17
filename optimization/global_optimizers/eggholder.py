# -*- coding: utf-8 -*-
# goptimzers.py

"""
Global optimization aims to find the global minimum of a function within given bounds,
in the presence of potentially many local minima. Typically, global minimizers efficiently
search the parameter space, while using a local minimizer (e.g., minimize) under the hood.

SciPy contains a number of good global optimizers. Here, we’ll use those on the same
objective function, namely the (aptly named) eggholder function.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    x = np.arange(-512, 513)
    y = np.arange(-512, 513)
    xgrid, ygrid = np.meshgrid(x, y)
    xy = np.stack([xgrid, ygrid])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(45, -45)
    ax.plot_surface(xgrid, ygrid, eggholder(xy), cmap='terrain')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('eggholder(x, y)')
    plt.show()


def eggholder(v):
    x, y = v
    return (-(y + 47) * np.sin(np.sqrt(abs(x/2 + (y+47)))) - x * np.sin(np.sqrt(abs(x - (y + 47)))))

bounds = [(-512, 512), (-512, 512)]

if __name__ == '__main__':
    main()