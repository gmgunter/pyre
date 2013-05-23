# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# simple types
from .Boolean import Boolean as bool
from .Decimal import Decimal as decimal
from .Float import Float as float
from .INet import INet as inet
from .Integer import Integer as int
from .Object import Object as identity
from .String import String as str

# more complex types
from .Date import Date as date
from .Dimensional import Dimensional as dimensional
from .Time import Time as time
from .URI import URI as uri

# containers
from .Sequence import Sequence as sequence
from .Array import Array as array
from .List import List as list
from .Set import Set as set
from .Tuple import Tuple as tuple


# put them in piles
basic = (identity, bool, decimal, float, inet, int, str)
composite = (date, dimensional, time, uri)
containers = (sequence, array, list, set, tuple)
# all of them
types = basic + composite + containers


# end of file 
