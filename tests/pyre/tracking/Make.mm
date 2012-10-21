# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity tracking

sanity:
	${PYTHON} ./sanity.py

tracking:
	${PYTHON} ./simple.py
	${PYTHON} ./lookup.py
	${PYTHON} ./command.py
	${PYTHON} ./file.py
	${PYTHON} ./fileregion.py
	${PYTHON} ./script.py
	${PYTHON} ./chain.py


# end of file 
