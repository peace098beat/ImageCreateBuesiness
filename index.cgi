#!/home/fififactory/.pyenv/versions/2.7.9/bin/python
#! coding:utf-8
import cgitb
# cgitb モジュールの enable() は、CGIスクリプトの実行時に発生したエラーの内容をブラウザに送信します
cgitb.enable()

from wsgiref.handlers import CGIHandler
from ImageCreateBuesiness.flaskr import app
#from testapp.testapp.flaskr import app

CGIHandler().run(app)

