from inspire import app, db
from config import visible, public_name, internal_name, blueprint, safe_name
from flask import Flask, request, flash, redirect
from flask import url_for, render_template, g, session

from inspire.main_database import User
from database import !!@@!!Dictionary


# Inspire pages should look like form
#@blueprint.route(<'/url'>)
#@blueprint.route(<'/alternate/url'>)
#@blueprint.route(<'/another/alternate/url'>)
#@app.inspire
#def <internal page name>():
#   ... User.query ...
#   ... g.user ...
#   ... flash('message') ...
#   return render_template(<'static page.html'>)


                        
@blueprint.route('/')
@app.inspire
def index():
    return render_template(internal_name+'/index.html')
    