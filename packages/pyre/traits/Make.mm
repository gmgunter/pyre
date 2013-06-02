# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


PROJECT = pyre
PACKAGE = traits
PROJ_CLEAN += $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Behavior.py \
    Dict.py \
    Facility.py \
    InputFile.py \
    OutputFile.py \
    Property.py \
    Slotted.py \
    Trait.py \
    properties.py \
    __init__.py


export:: export-package-python-modules

# end of file 
