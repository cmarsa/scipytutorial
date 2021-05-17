# -*- coding: utf-8 -*-
# ackley.py

"""Multimodal objective functions are those
thst gave multiple optima, such as a global optima
and manu local optima, or multiple global optima
with the same objective function output.

The Ackley function is an example of an objective
function that has a single global optima and multiple local optima
in which a local search might get stuck.
"""

from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # define range for input
    r_min, r_max = -5.0, 5.0
    # sample input range uniformly ay 01.increments
    xaxis = arange(r_min, r_max, 0.1)
    yaxis = arange(r_min, r_max, 0.1)
    # create a mesh from the axis
    x, y = meshgrid(xaxis, yaxis)
    # compute targets
    results = ackley(x, y)
    # create a surface plot
    figure = plt.figure()
    axis = figure.gca(projection='3d')
    axis.plot_surface(x, y, results, cmap='jet')
    # show the plot
    plt.show()


# ackley function
def ackley(x, y):
	return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


if __name__ == '__main__':
    main()