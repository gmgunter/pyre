#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Build a rudimentary table
"""


def test():
    import pyre.tabular

    class pricing(pyre.tabular.sheet):
        """
        The sheet layout
        """

        sku = pyre.tabular.measure()
        production = pyre.tabular.measure()
        shipping = pyre.tabular.measure()
        margin = pyre.tabular.measure()
        overhead = pyre.tabular.measure()
        discount = pyre.tabular.measure()

        cost = production + shipping
        msrp = (1 + margin + overhead)*cost

        price = msrp*(1 - discount)


    return pricing


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 
