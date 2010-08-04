#﻿# -*- coding: utf-8 -*-
################################################################################
##
##  Copyright 2010 Philipp Meier <pmeier82@googlemail.com>
##
##  Licensed under the EUPL, Version 1.1 or – as soon they will be approved by
##  the European Commission - subsequent versions of the EUPL (the "Licence");
##  You may not use this work except in compliance with the Licence.
##  You may obtain a copy of the Licence at:
##
##  http://ec.europa.eu/idabc/eupl
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the Licence is distributed on an "AS IS" basis,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the Licence for the specific language governing permissions and
##  limitations under the Licence.
##
################################################################################
# -*- coding: utf-8 -*-
#
# sim - noise/__init__.py
#
# Philipp Meier - <pmeier82 at googlemail dot com>
# 2010-01-21
#

"""noise generation package"""
__docformat__ = "restructuredtext"


##---IMPORTS

# packages
import scipy as N
from scipy import random as NR
from collections import deque
# own packages
from ar_model import ar_fit, ar_model_check_stable


##---CLASSES

class NoiseGen(object):
    """generic noise generator

    This noise generator will yield multivariate noise samples from a Gaussian
    with a given mean and covariance matrix.
    """

    # constructor
    def __init__(self, mu=None, sigma=None):
        """
        :Parameters:
            mu : ndarray
                1d-array, the mean of the distribution.
                Default=None
            sigma : ndarray
                2d-array, square matrix with same dims as mu. The covariance
                matrix of the distribution.
                Default=None
        """

        if mu is None:
            if sigma is None:
                mu = N.zeros(1)
            else:
                mu = N.zeros(sigma.shape[0])
        if sigma is None:
            sigma = N.eye(mu.size)

        # parameter checks
        if mu.ndim != 1 or sigma.ndim != 2:
            ValueError('expect mu 1dim and sigma 2dim square')
        if mu.size != sigma.shape[0] != sigma.shape[1]:
            ValueError('mu does not match sigma shape')

        # memebers
        self.nvar = mu.size
        self.mu = mu
        self.sigma = sigma

    # methods public
    def query(self, size=1):
        """return noise samples

        :Parameters:
            size : int
                Number of samples to produce.
                Default=1
        """

        return NR.multivariate_normal(
            self.mu,
            self.sigma,
            size
        )


class ArNoiseGen(NoiseGen):
    """multivariate noise process from an autoregressive model

    The process will produce samples from a zero mean, multivariate Gaussian.
    Samples have correlations across the multivariate components, temporal
    correlations within the components and also temporal correlations between
    the components.
    """

    # constructor
    def __init__(self, noise_params):
        """
        :Parameters:
            noise_params : tuple
                A tuple of length 1 or 2:
                len 1: A strip of data to estimate the model parameters from.
                len 2: A and C, the matching AR coefficient and channel covariance matrices.
        """

        # check parameters
        if len(noise_params) == 1:
            if not issubclass(noise_params[0].__class__, N.ndarray):
                raise ValueError('noise strip should be ndarray')
            A, C = ar_fit(noise_params[0])[:2]
        elif len(noise_params) == 2:
            if not issubclass(noise_params[0].__class__, N.ndarray) or \
            not issubclass(noise_params[1].__class__, N.ndarray):
                raise ValueError('A and C matrix should be ndarrays')
            A, C = noise_params
        else:
            raise ValueError('noise_params not tuple/list of len 1 or 2')

        # check model
        if A.shape[0] != C.shape[0] != C.shape[1]:
            raise ValueError('A and C matrix dont fit each other. %s and %s' %
                (str(A.shape), str(C.shape)))
        if ar_model_check_stable(A) is False:
            raise ValueError('estimated model is not stable')

        # super [zeros mean, multichannel white noise with covariance C]
        super(ArNoiseGen, self).__init__(mu=N.zeros(C.shape[0]), sigma=C)

        # members
        self.coeffs = A.T
        self.norder = self.coeffs.shape[0] / float(self.nvar)
        if self.norder != round(self.norder):
            raise ValueError('invalid model order (not integer?)')
        self.norder = int(self.norder)
        mem_size = self.norder * self.nvar
        self.coeffs_mem = deque([0] * mem_size, maxlen=mem_size)

        # run simulation for 5k samples to overcome initial oscillations
        self.query(5000)

    def query(self, size=1):
        """return noise samples

        :Parameters:
            size : int
                Number of samples to produce.
                Default=1
        """

        # super
        rval = super(ArNoiseGen, self).query(size=size)

        # generate noise
        for k in xrange(size):
            rval[k] += N.dot(self.coeffs_mem, self.coeffs)
            self.coeffs_mem.extendleft(rval[k, ::-1])
        return rval


##---MAIN

if __name__ == '__main__':
    pass