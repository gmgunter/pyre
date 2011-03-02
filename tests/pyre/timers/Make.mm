# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity python native pyre

sanity:
	${PYTHON} ./sanity.py

python:
	${PYTHON} ./python_timer.py
	${PYTHON} ./python_timer_errors.py

native:
	${PYTHON} ./native_timer.py

pyre:
	${PYTHON} ./pyre_timer.py

# end of file 
