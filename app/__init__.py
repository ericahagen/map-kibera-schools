# -*- coding: utf-8 -*-
"""
    app
    ~~~

    Static site generator for the Kibera School Project by Feedback Labs

    This file initializes the app and manages configuration before importing
    the other modules to do all the work.

"""

from flask import Flask

app = Flask('app', static_url_path='/static')

app.config['FREEZER_DESTINATION'] = app.config['BUILD_OUTPUT'] = '../output'
app.config['CONTENT_FOLDER'] = '../content'

from . import content
from . import views
from . import static
