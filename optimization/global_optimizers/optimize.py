# -*- coding: utf-8 -*-
# optimize.py

import numpy as np
from scipy import optimize
from numpy.random import randint
import matplotlib.pyplot as plt

from eggholder import eggholder
from eggholder import bounds


def main():

    results = {}
    results['shgo'] = optimize.shgo(eggholder, bounds)

    results['DA'] = optimize.dual_annealing(eggholder, bounds)

    results['DE'] = optimize.differential_evolution(eggholder, bounds)

    # basinhopping requires initiual guess x0
    x0 = np.array([randint(-512, 513), randint(-512, 513)])
    kwargs = {'bounds': bounds}
    results['BH'] = optimize.basinhopping(eggholder, x0, minimizer_kwargs=kwargs)

    # shgo has a second method, which returns all local minima rather
    # than only what it thinks is the global minimum:
    results['shgo_sobol'] = optimize.shgo(eggholder, bounds, n=200, iters=5,
                                          sampling_method='sobol')

    plot_minima(results)
    

def plot_minima(results):

    def plot_point(res, marker='o', color=None):
        ax.plot(512+res.x[0], 512+res.x[1], marker=marker, color=color, ms=10)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(-512, 513)
    y = np.arange(-512, 513)
    xgrid, ygrid = np.meshgrid(x, y)
    xy = np.stack([xgrid, ygrid])
    im = ax.imshow(eggholder(xy), interpolation='bilinear', origin='lower',
                   cmap='gray')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plot_point(results['BH'], color='y')
    plot_point(results['DE'], color='c')
    plot_point(results['DA'], color='w')

    # SHGO produces multiple minima, plot them all
    plot_point(results['shgo'], color='r', marker='+')
    plot_point(results['shgo_sobol'], color='r', marker='x')
    for i in range(results['shgo_sobol'].xl.shape[0]):
        ax.plot(512 + results['shgo_sobol'].xl[i, 0],
                512 + results['shgo_sobol'].xl[i, 1],
                'ro', ms=2)

    ax.set_xlim([-4, 514*2])
    ax.set_ylim([-4, 514*2])

    plt.show()


if __name__ == '__main__':
    main()