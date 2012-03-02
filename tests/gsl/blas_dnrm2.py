#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Exercise {dnrm2}
"""


def test():
    # externals
    import gsl
    import math
    # a value
    x = 3
    # make a couple of vectors
    v = gsl.vector(shape=10).fill(x)
    # compute the dot product
    assert gsl.blas.dnrm2(v) ==  math.sqrt(v.shape*x**2)
    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file 