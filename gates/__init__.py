'''Python stuff in here.'''

from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(10)

import gates.views