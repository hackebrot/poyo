# -*- coding: utf-8 -*-

import logging

from .exceptions import PoyoException
from .parser import parse_string

try:
    from logging import NullHandler
except ImportError:
    from logging import Handler

    class NullHandler(Handler):
        def emit(self, record):
            pass

__author__ = 'Raphael Pierzina'
__email__ = 'raphael@hackebrot.de'
__version__ = '0.4.1'

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = ['parse_string', 'PoyoException']
