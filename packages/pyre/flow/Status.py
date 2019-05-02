# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2019 all rights reserved
#


# externals
import weakref
# support
import pyre
import journal


# declaration
class Status(pyre.tracker):
    """
    A helper that watches over a component's traits and records value changes
    """


    # public data
    @property
    def dirty(self):
        """
        Return my current status
        """
        # easy enough
        return self._dirty

    @dirty.setter
    def dirty(self, status):
        """
        Adjust my status
        """
        # if i'm being marked as dirty
        if status is True:
            # flush
            return self.flush()
        # otherwise, just update the status
        self._dirty = False
        # all done
        return self


    # interface
    def track(self):
        """
        Start tracking my {node}
        """
        # get the client
        node = self.node()
        # chain up
        return super().track(component=node)


    def playback(self, alias):
        """
        Go through the history of the trait named {alias}
        """
        # get my client
        node = self.node()
        # find its trait by this name
        trait = node.pyre_trait(alias=alias)
        # get the key
        key = node.pyre_inventory[trait].key
        # chain up
        yield from super().playback(key=key)
        # all done
        return


    # meta-methods
    def __init__(self, node, dirty, **kwds):
        # chain up
        super().__init__(**kwds)
        # remember my clients
        self.node = weakref.ref(node)
        # enable tracking
        self.track()
        # initialize my flag
        self._dirty = dirty
        # all done
        return


    # hooks
    def flush(self, observable=None, **kwds):
        """
        Handler of the notification that the value of {observable} has changed
        """
        # get the client
        node = self.node()
        # show me
        print(f"flushing {node}")
        # mark me
        self._dirty = True
        # chain up
        return super().flush(observable=observable, **kwds)


    # implementation details
    # data
    _dirty = True


# end of file
