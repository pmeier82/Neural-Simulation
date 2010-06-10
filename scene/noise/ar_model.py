# -*- coding: utf-8 -*-
#
# sim - noise_gen.py
#
# Philipp Meier - <pmeier82 at gmail dot com>
# 2010-01-18
#
# $Id: ar_model.py 4602 2010-04-21 09:05:51Z phil $
#

"""noise generation with multivariate autoregressive models"""
__docformat__ = "restructuredtext"


##---IMPORTS

# packages
import scipy as N
from scipy import linalg as NL, random as NR


##---CONSTANTS

EPS = N.finfo(N.float64).eps


##---FUNCTIONS

def ar_fit(p_data, p_or_plist=range(100), selector='sbc'):
    """fits a (multivariate) AR (_A_uto_R_egrssive) model to data

    :Parameters:
        p_data : ndarray
            Data with observations on the rows and variables on the columns
        p_or_plist : list
            List of model orders to select from. This list has to be continuous
            with a step size of 1, e.g. [10,11,12,13,14]
        selector : str
            One of 'sbc' for the Schwarz Bayesian Criterion or 'fpe' for the
            log of Akaike's Final Prediction Error. This determines what metric
            is used to evaluate the best model order.
    """

    # checks and inits
    if not isinstance(p_data, N.ndarray):
        raise ValueError('p_data is not an ndarray')
    data = p_data.copy()
    n, m = data.shape
    if selector not in ['sbc', 'fpe']:
        raise ValueError('selector has to be one of: "sbc" or "fpe"!')
    if not isinstance(p_or_plist, list):
        p_or_plist = [p_or_plist]
    p_max = max(p_or_plist)
    ne = n - p_max
    npmax = m * p_max
    if ne <= npmax:
        raise ValueError('time series to short!')
    R = _ar_model_qr(data, p_max)

    # model order selection
    if len(p_or_plist) > 1:
        sbc, fpe, ldp, np = _ar_model_select(R, m, ne, p_or_plist)
        if selector == 'sbc':
            crit = sbc
        elif selector == 'fpe':
            crit = fpe
    else:
        crit = N.zeros(1)
    p_opt = crit.argmin()
    np = m * p_opt

    # get lower right triangle of R
    #
    #     | R11  R12 |
    # R = |          |
    #     |  0   R22 |
    #
    R11 = R[:np,:np]
    R12 = R[:np,npmax:]
    R22 = R[np:,npmax:]

    # build the model
    A = N.dot(NL.inv(R11), R12).T
    C = N.dot(R22.T, R22) / (ne - np)

    # return
    del R, R11, R12, R22
    return A, C, crit


def _ar_model_select(R, m, ne, p_range):
    """model order selection

    :Parameters:
        R : ndarray
            upper triangular mx from QR
        m : int
            state vector dimension
        ne : int
            number of bock equations of size m used in the estimation
        p_range : list
            list of model order to select from
    """

    # inits
    p_max = max(p_range)
    p_len = len(p_range)

    sbc = N.zeros(p_len)
    fpe = N.zeros(p_len)
    ldp = N.zeros(p_len)
    
    np = N.zeros(p_len)
    np[-1] = m * p_max

    # get lower right triangle of R
    #
    #     | R11  R12 |
    # R = |          |
    #     |  0   R22 |
    #
    R22 = R[np[-1]:np[-1]+m,:][:,np[-1]:np[-1]+m]
    invR22 = NL.inv(R22)
    Mp = N.dot(invR22, invR22.T)

    # model selection
    ldp[-1] = 2.0 * N.log(NL.det(R22))
    for i in reversed(xrange(p_len)):
        np[i] = m * p_range[i]
        if p_range[i] < p_max:
            
            # downdated part of R
            Rp = R[np[i]:np[i]+m,:][:,np[-1]:np[-1]+m]

            # woodbury formular
            L = NL.cholesky(N.eye(m) + N.dot(N.dot(Rp,Mp), Rp.T), lower=True)
            Np = N.dot(N.dot(NL.inv(L), Rp), Mp)
            Mp = Mp - N.dot(Np.T, Np)

            ldp[i] = ldp[i+1] + 2.0 * N.log(NL.det(L))

        # selector metrics
        sbc[i] = ldp[i]/m - N.log(ne) * (ne - np[i])/ne
        fpe[i] = ldp[i]/m - N.log(ne * (ne - np[i])/(ne + np[i]))

    # return
    return sbc, fpe, ldp, np


def _ar_model_qr(data, p=1):
    """QR factorization for a (multivariate) zero-mean AR model

    :Parameters:
        data : ndarray
            data with observations on the rows and variables on the columns
        p : int or list
            the model order, how many samples to regress over
    """

    # inits
    n, m = data.shape            # observations, channels
    ne = n - p                   # number of block equations of size m
    np = m * p                   # number of parameter vectors of size m
    K = N.zeros((ne, np + m))  # the lag shifted data matrix
    
    # compute predictors
    for i in xrange(p):
        K[:,m*i:m*(i+1)] = data[p-i-1:n-i-1,:]
    K[:,np:np+m] = data[p:n,:]

    # contition the matrix and factorize
    scale = N.sqrt( ((np+m)**2 + np + m + 1) * EPS)
    R = NL.qr(
        N.concatenate((
            K,
            scale * N.diag([NL.norm(K[:,i]) for i in xrange(K.shape[1])])
        )),
        mode='r'
    )
    
    # return
    del K
    return R


def _ar_model_sim(A, C, n=1, n_discard=0, mean=None, check=False):
    """simulates data for a VARMA model

    :Parameters:
        A : ndarray
            AR Coeffitient matrix
        C : ndarray
            Noise covariance matrix
        n : int
            Number od datapoints to simulate with the process
        n_discard : int
            Number od datapoints to discard befor taking datapoints for the
            simulation.
        mean : ndarray
            Mean vector for the process
    """

    # inits and checks
    if mean is None:
        mean = N.zeros(A.shape[0])
    else:
        if mean.size != A.shape[0]:
            raise ValueError('mean vector has wrong shape!')
    m = C.shape[0]
    p = A.shape[1] / m
    if p != round(p):
        raise ValueError('Bad arguments, p not an integer! %s' % p)

    # check for stable model
    if check is True:
        ar_model_check_stable(A)

    # generate data
    err = NR.multivariate_normal(mean, C, n_discard + n)
    x = N.zeros((p, m))
    rval = N.zeros((p + n_discard + n, m))
    
    for k in xrange(p, p + n_discard + n):
        for j in xrange(p):
            x[j,:] = N.dot(rval[k-j-1,:], A[:,j*m:(j+1)*m])
        rval[k,:] = x.sum(axis=0) + err[k-p,:]

    # return
    return rval[p+n_discard:,:]


def ar_model_check_stable(A):
    """check if this AR model is stable

    :Parameters:
        A : ndarray
            The coefficient matrix of the model
    """

    # inits and checks
    m, p = A.shape
    p /= m
    if p != round(p):
        raise ValueError('bad inputs!')

    # check for stable model
    A1 = N.concatenate((
        A,
        N.concatenate((
            N.eye((p-1)*m),
            N.zeros(((p-1)*m, m))
        ), axis=1)
    ))
    lambdas = NL.eigvals(A1)
    rval = True
    if (N.absolute(lambdas) > 1).any():
        rval = False
    del A1, lambdas
    return rval


def get_noise_sample(idx=None, size=None, filename=None):
    """get some noise from a recording of maquaque prefrontal cortex"""
    
    # inits and checks
    if filename is None:
        filename = '/home/phil/monkey-data/Louis/L011/L0110985.xpd'
    if size is None:
        size = 10000
    
    # load data
    from spike.util.datafile import XpdFile
    data = XpdFile(filename).get_data(item=15)

    # return
    if size >= data.shape[0]:
        size = data.shape[0] - 1
        idx = 0
    if idx is None:
        idx = NR.randint(data.shape[0] - size)
    return data[idx:idx+size].copy()


##---MAIN

if __name__ == '__main__':

    noise = get_noise_sample()
    noise = noise.astype('float64')
    noise = noise[:10000,:]
    
    A, C, c = ar_fit(noise)

    from spike.gui.plot import P, dataplot
    P.interactive(True)
    X = _ar_model_sim(A, C, 10000, 0, check=True)
    dataplot(noise)
    dataplot(X)

    from spike.util import TimeSeriesCovE
    TS_noise = TimeSeriesCovE(tf=65)
    TS_noise.update(noise)
    P.matshow(TS_noise.get_covmx())
    P.colorbar(boundaries=range(-5,16))

    TS_X = TimeSeriesCovE(tf=65)
    TS_X.update(X)
    P.matshow(TS_X.get_covmx())
    P.colorbar(boundaries=range(-5,16))
