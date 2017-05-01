import numpy as np

def gradU(data, minibatch, beta):
    
    dataX = data[:,:-1] 
    dataY = data[:,-1]
    dataX = np.c_[np.ones_like(dataX[:,0]), dataX]
    beta_X = (beta*dataX).sum(axis=1)
    
    der_temp = ((-1.)**dataY)/(1. + (np.exp( ((-1.)**(dataY+1.)) * beta_X )) )
    ddata = (der_temp[:, None] * dataX)
    ##### using minibatch of the data #####
    ddata = ddata[np.random.choice(ddata.shape[0], int(minibatch * ddata.shape[0]), replace=False),:].sum(axis=0) 
    #################################
    

    
    return (1./minibatch)*ddata  #minibatch
