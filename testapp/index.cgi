#!/home/fififactory/.pyenv/versions/3.4.2-flask/bin/python
 
import cgitb
cgitb.enable()
 
from wsgiref.handlers import CGIHandler
from testapp.flaskr import app
CGIHandler().run(app)