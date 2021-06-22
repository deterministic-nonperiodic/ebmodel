import numpy as np

def _sigmoid(x, s0, s1, c):
    #
    return s0 + s1 / (1.0 + np.exp(c*x))
    # return s0 + 0.5*s1*(1.0 + np.tanh(c*x))

def ln_ln(x):
    return 1.0 - np.exp(-np.exp(x))

def legendreP0(x):
    """The 0th Legendre polynomial."""
    return x

def legendreP2(x):
    """The second Legendre polynomial."""
    return (3.0*x**2 - 1.0) / 2.0

def solar_dist(x):
    return (5.0 - 3.0 * x**2) / 4.0

# store in a dictionary:
distribution = {
    'p0':legendreP0,
    'p2': legendreP2,
    's0':solar_dist
}

def _set_initial(x, x0, x1, d='p2'):
    #
    return x0 + x1 * distribution[d](x)
