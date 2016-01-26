#!/home/fififactory/.pyenv/versions/2.7.9/bin/python

import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from ImageCreateBuesiness.flaskr import app
CGIHandler().run(app)

