# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import pyre
from pyre.components.Component import Component
from Functor import Functor


class Gaussian(Component, family="gauss.functors.gaussian", implements=Functor):
    """
    An implementation of the normal distribution with mean #@$\mu$@ and variance #@$\sigma^2$@
    """

    # public state
    mean = pyre.components.array()
    mean.aliases.add("μ")
    mean.doc = "the position of the mean of the Gaussian distribution"
    mean.default = [0.0]

    spread = pyre.components.float()
    spread.aliases.add("σ")
    spread.doc = "the variance of the Gaussian distribution"
    spread.default = 1.0


    @pyre.components.export
    def eval(self, points):
        """
        Compute the value of the gaussian
        """
        # access the math symbols
        from math import exp, sqrt, pi as π
        # cache the inventory items
        μ = self.μ
        σ = self.σ
        # precompute the normalization factor
        normalization = 1 / sqrt(2*π) / σ
        # and the scaling of the exposnential
        scaling = 2 * σ**2
        # loop over points and yield the computed value
        for x in points:
            # compute |x - μ|^2
            # this works as long as x and μ have the same length
            r2 = sum((x_i - μ_i)**2 for x_i, μ_i in zip(x, μ))
            # yield the value at the xurrent x
            yield normalization * exp(- r2 / scaling)

        return


# end of file 
