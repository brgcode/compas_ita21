"""
********************************************************************************
compas_ita21
********************************************************************************

.. currentmodule:: compas_ita21


.. toctree::
    :maxdepth: 1

    compas_ita21.datastructures
    compas_ita21.rhino

"""

from __future__ import print_function

import os


__author__ = ["tom van mele"]
__copyright__ = "ETH Zurich"
__license__ = "MIT License"
__email__ = "van.mele@arch.ethz.ch"
__version__ = "0.1.0"


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]
