# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity nodes

sanity:
	${PYTHON} ./sanity.py

nodes:
	${PYTHON} ./node.py


# end of file 
