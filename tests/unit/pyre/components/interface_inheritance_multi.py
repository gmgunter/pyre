#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Exercise multiple inheritance among interfaces
"""


def test():
    # access
    import pyre.components
    from pyre.components.Interface import Interface
    from pyre.components.Property import Property

    # declare an interface hierarchy
    class base(Interface):
        # traits
        common = Property()
        common.default = "base"

        a1 = Property()
        a1.default = "base"

        a2 = Property()
        a2.default = "base"

    class a1(base):
        # traits
        a1 = Property()
        a1.default = "a1"

    class a2(base):
        # traits
        a2 = Property()
        a2.default = "a2"

    class derived(a1, a2):
        """a derived interface"""
        common = Property()
        common.default = "derived"

        extra = Property()
        extra.default = "derived"
        
    # check that everything is as expected with the hierachy
    assert base._pyre_configurables == (base, Interface)
    assert a1._pyre_configurables == (a1, base, Interface)
    assert a2._pyre_configurables == (a2, base, Interface)
    assert derived._pyre_configurables == (derived, a1, a2, base, Interface)

    # check the _pyre_Inventory constructions
    # first the expected inheritance relations
    assert issubclass(base._pyre_Inventory, Interface._pyre_Inventory)
    assert issubclass(a1._pyre_Inventory, base._pyre_Inventory)
    assert issubclass(a1._pyre_Inventory, Interface._pyre_Inventory)
    assert issubclass(a2._pyre_Inventory, base._pyre_Inventory)
    assert issubclass(a2._pyre_Inventory, Interface._pyre_Inventory)
    assert issubclass(derived._pyre_Inventory, a1._pyre_Inventory)
    assert issubclass(derived._pyre_Inventory, a2._pyre_Inventory)
    assert issubclass(derived._pyre_Inventory, base._pyre_Inventory)
    assert issubclass(derived._pyre_Inventory, Interface._pyre_Inventory)
    # and, more thoroughly, the __mro__
    assert base._pyre_Inventory.__mro__ == (
        base._pyre_Inventory,
        Interface._pyre_Inventory, object)
    assert a1._pyre_Inventory.__mro__ == (
        a1._pyre_Inventory, base._pyre_Inventory,
        Interface._pyre_Inventory, object)
    assert a2._pyre_Inventory.__mro__ == (
        a2._pyre_Inventory, base._pyre_Inventory,
        Interface._pyre_Inventory, object)
    assert derived._pyre_Inventory.__mro__ == (
        derived._pyre_Inventory, a1._pyre_Inventory, a2._pyre_Inventory, base._pyre_Inventory,
        Interface._pyre_Inventory, object)

    # access the traits of base
    assert base.common._pyre_category == "properties"
    assert base.common.default == "base"
    assert base.a1._pyre_category == "properties"
    assert base.a1.default == "base"
    assert base.a2._pyre_category == "properties"
    assert base.a2.default == "base"
    # access the traits of a1
    assert a1.common._pyre_category == "properties"
    assert a1.common.default == "base"
    assert a1.a1._pyre_category == "properties"
    assert a1.a1.default == "a1"
    assert a1.a2._pyre_category == "properties"
    assert a1.a2.default == "base"
    # access the traits of a2
    assert a2.common._pyre_category == "properties"
    assert a2.common.default == "base"
    assert a2.a1._pyre_category == "properties"
    assert a2.a1.default == "base"
    assert a2.a2._pyre_category == "properties"
    assert a2.a2.default == "a2"
    # access the traits of derived
    assert derived.common._pyre_category == "properties"
    assert derived.common.default == "derived"
    assert derived.a1._pyre_category == "properties"
    assert derived.a1.default == "a1"
    assert derived.a2._pyre_category == "properties"
    assert derived.a2.default == "a2"
    assert derived.extra._pyre_category == "properties"
    assert derived.extra.default == "derived"

    # make sure derivation did not cause any pollution
    try:
        base.extra
        assert False
    except AttributeError:
        pass

    return base, a1, a2, derived
     

# main
if __name__ == "__main__":
    test()


# end of file 
