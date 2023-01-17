def cac(pathMic1, pathMic2, freqSamples):
    import numpy as np
    import pandas as pd
    rho0 = 1.2
    c = 343
    f = np.linspace(377, 3400, freqSamples)
    k = 2 * np.pi * f[:] / c
    L = 33 / 100
    x1 = 10 / 100
    s = 3.75 / 100
    p1 = np.loadtxt(pathMic1, usecols=[1, 2])
    p2 = np.loadtxt(pathMic2, usecols=[1, 2])
    p1 = p1[:, 0] + p1[:, 1] * 1j
    p2 = p2[:, 0] + p2[:, 1] * 1j
    H12 = p2 / p1
    Hh = np.exp(-1j * k * s)
    Hr = np.exp(1j * k * s)
    r = np.abs(((H12 - Hh) / (Hr - H12)) * np.exp(1j * 2 * k * (x1)))
    alpha = 1 - r**2
    dfOut = np.c_[f, alpha]
    return pd.DataFrame(dfOut, columns=['f', 'alpha'])