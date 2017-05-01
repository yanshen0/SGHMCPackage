import numpy as np


def U(data, beta):
    dataX = data[:,:-1] 
    dataY = data[:,-1]
    dataX = np.c_[np.ones_like(dataX[:,0]), dataX]
    beta_X = (beta*dataX).sum(axis=1)
    pdata = (np.log(1. + np.exp( ((-1.)**dataY) * beta_X) )).sum() 
    return pdata
