'''Python stuff in here.'''

from flask import Flask

from equinox.utils import *

app = Flask(__name__)

import equinox.views