import numpy as np
from .initial import _sigmoid

def cons_albedo(x, warm_a, pm):
    return warm_a


def sigm_albedo(x, warm_a, pm):

    delta_a = pm['a0'] - pm['ai']
    delta_temp = x - 0.5 * (pm['Tf'] + pm['Tsn'])
    albedo = _sigmoid(delta_temp, pm['ai'], delta_a, 0.5)
    
    return np.where(x < pm['Tsn'], albedo, warm_a)

def step_albedo(x, warm_a, pm):
    return np.where(x < pm['Tf'], pm['ai'], warm_a)


def linr_albedo(x, warm_a, pm):

    idx_0 = np.argmin( abs(x - pm['Tsn']) )
    delta_a = pm['ai'] - warm_a[idx_0]

    snow_slope = delta_a / (pm['Tf'] - pm['Tsn'])
    cnd0 = x <= pm['Tf']
    mask = (~cnd0) & (x < pm['Tsn'])

    albedo = np.where(cnd0, pm['ai'], warm_a)
    albedo[mask] = warm_a[idx_0] + snow_slope*(x[mask] - pm['Tsn'])

    return albedo

# def sellers_albedo(x, warm_a, pm):
#     delta_a = pm['aw'] - pm['as']
#     delta_temp = x - (pm['Tf'] + d)
#     albedo = 
#     albedo+=     
#     return np.where(x < pm['Tsn'], albedo, warm_a)

albedo_form = {
        'sigm': sigm_albedo,
        'step': step_albedo,
        'lins': linr_albedo,
        'cons': cons_albedo
}