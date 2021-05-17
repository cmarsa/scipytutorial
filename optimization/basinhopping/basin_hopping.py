# -*- ooding: utf-8 -*-
# basin_gopping.py

from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy.random import rand
from scipy.optimize import basinhopping

def main(function):
    # define range for input
    r_min, r_max = -5.0, 5.0
    # define the starting point as a random sample from
    # the domain
    pt = r_min + rand(2) * (r_max- r_min)
    # perform the basin hopping search
    result = basinhopping(function, pt, stepsize=0.5, niter=200)
    # summarize the result
    print(f'status: {result["message"]}')
    print(f'total evaluations: {result["nfev"]:d}')
    # evaluate solution
    solution = result['x']
    evaluation = function(solution)
    print(f'solution: f({solution}) = {evaluation:.5f}')



# ackley function
def ackley(v):
    x, y = v
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


# himmelblau function
def himmelblau(v):
    x, y = v
    return (x**2 + y - 11)**2 + (x + y**2 -7)**2


if __name__ == '__main__':
    main(ackley)