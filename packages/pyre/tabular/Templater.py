# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import itertools
import collections
from ..patterns.AttributeClassifier import AttributeClassifier


class Templater(AttributeClassifier):
    """
    Metaclass that inspects sheet declarations
    """


    # types
    from .Record import Record
    from .Measure import Measure
    from .Derivation import Derivation


    # meta methods
    def __new__(cls, name, bases, attributes, **kwds):
        """
        Build a new worksheet record
        """
        # harvest the locally declared fields from the class declaration
        localMeasures = tuple(cls.pyre_harvest(attributes, cls.Measure))
        localDerivations = tuple(cls.pyre_harvest(attributes, cls.Derivation))

        # set up the attributes
        attributes["pyre_name"] = name
        attributes["pyre_localMeasures"] = localMeasures
        attributes["pyre_localDerivations"] = localDerivations
        attributes["pyre_inheritedMeasures"] = ()
        attributes["pyre_inheritedDerivations"] = ()
        
        # build the record
        sheet = super().__new__(cls, name, bases, attributes, **kwds)

        # extract the inherited measures from the superclasses
        inheritedMeasures = []
        inheritedDerivations = []
        # prime the set of known names
        known = set(attributes)
        # iterate over my ancestors
        for base in sheet.__mro__[1:]:
            # narrow the search down to subclasses of Record
            if isinstance(base, cls):
                # loop over this ancestor's local fields
                for field in base.pyre_localMeasures:
                    # skip this field if it is shadowed
                    if field.name in known: continue
                    # otherwise save it
                    inheritedMeasures.append(field)
                # loop over this ancestor's local derivations
                for field in base.pyre_localDerivations:
                    # skip this field if it is shadowed
                    if field.name in known: continue
                    # otherwise save it
                    inheritedDerivations.append(field)
            # in any case, add the attributes of this base to the known pile
            known.update(base.__dict__)
        # attach the inherited fields to the sheet
        sheet.pyre_inheritedMeasures = tuple(inheritedMeasures)
        sheet.pyre_inheritedDerivations = tuple(inheritedDerivations)

        # create the Record subclass that holds the data
        recordName = name + "_record"
        recordBases = (cls.Record, )
        recordAttributes = collections.OrderedDict((item.name, item) for item in sheet.pyre_items())
        recordType = type(recordName, recordBases, recordAttributes)

        # attach it to the sheet
        sheet.pyre_Record = recordType

        # return the class record
        return sheet


    def __init__(self, name, bases, attributes, **kwds):
        """
        Initialize a newly minted worksheet class
        """
        # initialize the record
        # print("Templater.__init__: initializing a new sheet class")
        super().__init__(name, bases, attributes, **kwds)
        # and return
        return


    def __call__(self, **kwds):
        """
        Build a new sheet
        """
        # create the sheet
        # print("Templater.__call__: building a new sheet instance")
        sheet = super().__call__(**kwds)
        # and return it
        return sheet



# end of file 
