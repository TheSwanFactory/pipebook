import os
import sys
PKG_NAME='pipebook'

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '.', f'./{PKG_NAME}', '..', f'../{PKG_NAME}'
)))

from pipebook import *
from fridaay import *
