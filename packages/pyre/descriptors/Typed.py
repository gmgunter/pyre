# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# externals
import collections
# my base class is from {pyre.schemata}
from ..schemata.Type import Type


# declaration
class Typed(Type):
    """
    Mix-in class that encapsulates type information. Its instances participate in value
    conversions from external representations to python internal forms.
    """


    # public data
    # value preprocessors
    converters = ()
    # value post processors
    normalizers = ()
    # consistency checks
    validators = ()


    # interface
    def coerce(self, value, **kwds):
        """
        Walk {value} through the steps from raw to validated
        """
        # {None} is special; leave it alone
        if value is None: return None
        # otherwise, convert
        for converter in self.converters: value = converter(value=value, **kwds)
        # cast
        value = super().coerce(value=value, **kwds)
        # normalize
        for normalizer in self.normalizers: value = normalizer(value=value, **kwds)
        # validate
        for validator in self.validators: value = validator(value=value)
        # and return the new value
        return value


    # framework requests
    def attach(self, **kwds):
        """
        Called by my client to let me know that all the available meta-data have been harvested
        """
        # repair convenient usage that breaks my representation constraints: make sure my value
        # processors are iterable
        self.converters = self.listify(self.converters)
        self.normalizers = self.listify(self.normalizers)
        self.validators = self.listify(self.validators)

        # chain up
        return super().attach(**kwds)


    # meta methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # initialize my value processors to something modifiable
        self.converters = []
        self.normalizers = []
        self.validators = []

        # all done
        return
    

    # implementation details
    def listify(self, processors):
        """
        Make sure {processors} is an iterable regardless of what the user left behind
        """
        # handle anything empty
        if not processors: return []
        # if i have an iterable
        if isinstance(processors, collections.Iterable):
            # turn it into a list
            return list(processors)
        # otherwise, place the lone processor in a list
        return [processors]


# end of file 
