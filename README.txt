===========
sghmc
===========

sghmc has sghmc, hmc, U, gradU

    #!/usr/bin/env python

    from sghmc import sghmc
    from sghmc import hmc
    from sghmc import U
    from sghmc import gradU


    sghmc(gradU, eta, L, alpha, x, V)
    hmc(U, gradU, m, dt, nstep, x, MH)
    gradU(data, minibatch, beta)
    U(data, beta)
    
