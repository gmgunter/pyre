#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Build a table hierarchy with single inheritance
"""


def test():
    import pyre.tabular

    class raw(pyre.tabular.sheet):
        """
        The sheet layout
        """

        sku = pyre.tabular.measure()
        production = pyre.tabular.measure()
        shipping = pyre.tabular.measure()
        margin = pyre.tabular.measure()
        overhead = pyre.tabular.measure()
        discount = pyre.tabular.measure()

    class pricing(raw):

        cost = raw.production + raw.shipping
        msrp = (1 + raw.margin + raw.overhead)*cost
        price = msrp*(1 - raw.discount)


    # check the base
    assert raw.pyre_name == "raw"
    assert raw.pyre_localItems == (
        raw.sku, raw.production, raw.shipping, raw.margin, raw.overhead, raw.discount
        )
    assert raw.pyre_items == raw.pyre_localItems
    assert raw.pyre_measures == (
        raw.sku, raw.production, raw.shipping, raw.margin, raw.overhead, raw.discount
        )
    assert raw.pyre_derivations == ()

    
    # check the subclass
    assert pricing.pyre_name == "pricing"

    assert pricing.pyre_localItems == (
        pricing.cost, pricing.msrp, pricing.price
        )
    assert pricing.pyre_items == (
        pricing.sku, pricing.production, pricing.shipping, pricing.margin,
        pricing.overhead, pricing.discount,
        pricing.cost, pricing.msrp, pricing.price
        )
    assert pricing.pyre_measures == (
        pricing.sku, pricing.production, pricing.shipping, pricing.margin,
        pricing.overhead, pricing.discount,
        )
    assert pricing.pyre_derivations == (
        pricing.cost, pricing.msrp, pricing.price
        )

    return pricing, raw


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 
