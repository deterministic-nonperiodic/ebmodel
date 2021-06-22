# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:06:18 2017

@author: yan
"""
import numpy as np
from scipy import optimize, gradient
from datetime import datetime, timedelta
from scipy.integrate import simps

# some wrappers from numpy/scipy:

def fsolve(fun, x0, maxiter=100, jacobian=None, tol=1.0e-12, verbose=True):
    #
    result = optimize.root(fun, x0, method='hybr', jac=jacobian, tol=tol)

    if verbose:
        print('INFO:', result.message)
        print('SUM NRI:', np.sum(result.fun))

    return result.x


def compute_gradient(x, var, axis=-1):
    return gradient(var, x, edge_order=2, axis=axis)


# Runge-Kuta solvers in Shu-Osher form:
coefficients = {
    # Wicker & Skamarock:
    'ssp33': [[1.0, 0.0, 1.0],
              [0.75, 0.25, 0.25],
              [1./3., 2./3., 2./3.]],
    # classic Heun (midpoint) method:
    'ssp22': [[1.0,0.0,1.0], [0.50,0.50,0.50]],
    # 'dopri':
    }

str_fmt = 'prog: {:.4f}, vmin: {:.4f}, vmax: {:.4f}, update: {:6e}'

def rk_solver(rhs, sol, sim_time=1.0, dt=0.2,
              ftol=1e-6, method='ssp33'):
    '''
        rhs: callable ODE system returns n-dimensional derivatives:
        sol: initial condition nd-array
        ftol: stopping criteria (just for convergent systems)
    '''
    time = 0.0
    stop = False
    while not stop:
        
        sol_k = sol.copy()
        for ck, cn, cr in coefficients[method]:

            rhs_eval = dt * rhs(sol)
            sol = ck*sol_k + cn*sol + cr * rhs_eval

        # Stoping criteria:
        time += dt
        tend = np.abs(rhs_eval).max()

        stop = time > sim_time or tend < ftol

    if tend > ftol:
        print('INFO: Convergence was not achieved')

    return time, sol