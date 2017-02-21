#!/usr/bin/env python
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/psf/license for licensing details.

from __future__ import absolute_import

__author__ = "Sorin Sbarnea"
__copyright__ = "Copyright 2010-2013, Sorin Sbarnea"
__email__ = "sorin(dot)sbarnea(at)gmail.com"
__status__ = "Production"

from confluence.version import __version__, __date__

from confluence.confluence import Confluence

__all__ = ['confluence']

"""
Tendo is tested with Python 2.6-3.2
"""

import sys
if sys.hexversion < 0x02050000:
    sys.exit("Python 2.6 or newer is required by confluence module.")
