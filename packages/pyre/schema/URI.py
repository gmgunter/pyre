# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import re


# the declaration
class URI:
    """
    Parser for resource identifiers
    """


    # types
    from .exceptions import CastingError


    # public data
    @property
    def uri(self):
        """
        Assemble a string from my parts
        """
        parts = []
        # if I have a scheme
        if self.scheme: parts.append('{}:'.format(self.scheme))
        # if I have an authority
        if self.authority: parts.append('//{}'.format(self.authority))
        # if I have an address
        if self.address: parts.append('{}'.format(self.address))
        # if I have a query
        if self.query: parts.append('?{}'.format(self.query))
        # if I have a fragment
        if self.fragment: parts.append('#{}'.format(self.fragment))
        # assemble and return
        return ''.join(parts)


    # interface
    @classmethod
    def coerce(cls, value, **kwds):
        """
        Attempt to convert {value} into a internet address
        """
        # if {value} is one of mine
        if isinstance(value, cls):
            # leave it alone
            return value
        # if it is a string
        if isinstance(value, str):
            # parse it
            match = cls._regex.match(value)
            # if unsuccessful
            if match:
                # build a URI object
                uri = cls(
                    scheme=match.group('scheme'),
                    authority=match.group('authority'),
                    address=match.group('address'),
                    query=match.group('query'),
                    fragment=match.group('fragment')
                    )
                # and return it
                return uri
        # otherwise
        msg = 'unrecognizable URI {!r}'.format(value)
        raise cls.CastingError(value=value, description=msg)


    def clone(self):
        """
        Make a copy of me
        """
        return type(self)(
            scheme=self.scheme, authority=self.authority, address=self.address,
            query=self.query, fragment=self.fragment)
        

    # support for building nodes
    @classmethod
    def macro(cls, model):
        """
        Return my preferred macro factory
        """
        # by default, i build interpolations
        return model.interpolation
    

    # meta methods
    def __init__(self, scheme=None, authority=None, address=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.address = address
        self.query = query
        self.fragment = fragment
        return


    def __str__(self):
        # easy enough
        return self.uri


    # private data
    _regex = re.compile(
        "".join(( # adapted from http://regexlib.com/Search.aspx?k=URL
                r"^(?=[^&])", # disallow '&' at the beginning of uri
                r"(?:(?P<scheme>[^:/?#]+):)?", # grab the scheme
                r"(?://(?P<authority>[^/?#]*))?", # grab the authority
                r"(?P<address>[^?#]*)", # grab the address, typically a path
                r"(?:\?(?P<query>[^#]*))?", # grab the query, i.e. the ?key=value&... chunks
                r"(?:#(?P<fragment>.*))?"
                )))


    # public data
    __slots__ = ( 'scheme', 'authority', 'address', 'query', 'fragment' )


# end of file 