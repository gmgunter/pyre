# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# superclass
from .Processor import Processor


# declaration
class Normalizer(Processor):
    """
    A record method decorator that registers this method as a normalizer of descriptor values
    """


    # meta-methods
    def __call__(self, method):
        """
        Add {method} as a normalizer to my registered descriptors
        """
        # go through the sequence of registered descriptors
        for descriptor in self.descriptors:
            # and register {method} as a normalizer
            descriptor.normalizers.append(method)
        # all done
        return method
    

# end of file 