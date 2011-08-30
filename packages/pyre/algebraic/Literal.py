# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Node import Node


class Literal(Node):
    """
    Wrapper around foreign values that endows them with {Node} interface
    """


    # traversal of the nodes in my expression graph
    @property
    def dependencies(self):
        """
        Traverse my expression graph looking for nodes i depend on
        """
        # literals don't count as true dependencies
        return []


    # interface
    def eval(self, **kwds):
        """
        Compute my value
        """
        # easy enough...
        return self.value


    # meta methods
    def __init__(self, value, **kwds):
        super().__init__(**kwds)
        self.value = value
        return


    def __str__(self):
        return "{.value!r}".format(self)


# end of file 
