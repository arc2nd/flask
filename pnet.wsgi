#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/wsgi_scripts//sk")

from app.routes import app as application
application.secret_key = 'thisisatest'
