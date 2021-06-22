import os
from sklearn.externals import joblib

def create_path(path):
    try:
        os.makedirs(path)
    except:
        pass
    return path

def save_model(model, filename='model'):
    '''
        Function for saving a python object
    '''
    if isinstance(filename, str):

        with open(filename, mode='wb') as to_file:
            joblib.dump(model, to_file)
    else:
        raise ValueError('Argument `filename` must be a string')

def load_model(filename):
    #
    if os.path.exists(filename):
        with open(filename, mode='rb') as from_file:
            return joblib.load(from_file)
    else:
        raise ValueError('File: ' + filename + ' does not exist')
