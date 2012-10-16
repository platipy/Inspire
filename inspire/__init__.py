from __future__ import with_statement

# Flask stuff
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
     
# Import database call
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing
     
# Bootstrap stuff
from flask_bootstrap import Bootstrap
     
# Configuration constants are in the config module
import config

# Actual app creation
app = Flask(__name__)
app.config.from_object(config.FlaskConfig)
app.jinja_env.add_extension('jinja2.ext.do')
Bootstrap(app)

db = SQLAlchemy(app)
import inspire.database
import inspire.pages