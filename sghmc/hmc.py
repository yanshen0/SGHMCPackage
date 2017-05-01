import numpy as np

def hmc(U, gradU, m, dt, nstep, x, MH):
    p = np.random.randn(len(x)) * np.sqrt(m)
    oldX = x.copy()
    oldEnergy = 0.5 * (1./m) * p.dot(p)  + U(x)
    for i in range(nstep):
        p -= gradU(x) * dt/2.
        x +=  1./m * p * dt
        p -= gradU(x) * dt/2.
    newEnergy = 0.5 * (1./m) * p.dot(p)  + U(x)
    
    if MH and np.random.random() > np.exp(oldEnergy - newEnergy): # Metropolis-Hastings
        x = oldX.copy()
    return x.copy()
