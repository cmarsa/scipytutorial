# -*- coding: utf-8 -*-
# himmelblau.py
"""
The Himmelblau function is an example of an objective function
that has multiple global optima.

Specifically, it has four optima and each has the same objective
function evaluation. It is a two-dimensional objective function
that has a global optima at [3.0, 2.0], [-2.805118, 3.131312],
[-3.779310, -3.283186], [3.584428, -1.848126].

This means each run of a global optimization algorithm may
find a different global optima.
"""
from numpy import arange
from numpy import meshgrid
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # define range for input
    r_min, r_max = -5.0, 5.0
    # sample input range uniformly ast 0.1 increments
    xaxis = arange(r_min, r_max, 0.1)
    yaxis = arange(r_min, r_max, 0.1)
    # create a mesh from the axis
    x, y = meshgrid(xaxis, yaxis)
    # compute targets
    results = himmelblau(x, y)
    # create a surface plot
    figure = plt.figure()
    axis = figure.gca(projection='3d')
    axis.plot_surface(x, y, results, cmap='jet')
    # show results
    plt.show()


def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 -7)**2


if __name__ == '__main__':
    main()