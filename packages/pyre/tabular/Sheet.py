# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import itertools
from .Templater import Templater


class Sheet(metaclass=Templater):
    """
    The base class for worksheets
    """


    # public data
    pyre_name = None # the name of the sheet
    pyre_data = None # the list of records


    # interface
    def append(self, record):
        """
        Add {record} to my data set
        """
        # update my indices
        # what's the right thing to do when a new record with a key conflict shows up?
        # add the record to the data set
        self.pyre_data.append(record)
        # return 
        return self
        

    # introspection
    @classmethod
    def pyre_measures(cls):
        """
        Return an iterable over the entire set of my measures
        """
        return itertools.chain(cls.pyre_localMeasures, cls.pyre_inheritedMeasures)


    @classmethod
    def pyre_derivations(cls):
        """
        Return an iterable over the entire set of my derivations
        """
        return itertools.chain(cls.pyre_localDerivations, cls.pyre_inheritedDerivations)


    @classmethod
    def pyre_items(cls):
        """
        Return an iterable over the entire set of both my measures and my derivations
        """
        return itertools.chain(cls.pyre_measures(), cls.pyre_derivations())


    # meta methods
    def __init__(self, name=None, **kwds):
        super().__init__(**kwds)

        self.pyre_name = name
        self.pyre_data = []

        return


    def __iter__(self):
        """
        Build an iterator over my data set
        """
        return iter(self.pyre_data)


# end of file 
