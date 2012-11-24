from inspire import app, db
from config import visible, public_name, internal_name, blueprint
from flask import Flask, request, flash, redirect
from flask import url_for, render_template, g, session

from inspire.main_database import User
from database import Dictionary


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
    return render_template('index.html')

@blueprint.route('/points')
@blueprint.route('/points/')
@app.inspire
def view_points():
    dictionary_query = Dictionary.query.filter_by(key == 'points').all()
    lines = ""
    for dictionary in dictionary_query:
        name = "<b>%s</b>: " % dictionary.user.name
        points = "%d<br>" % dictionary.value
        lines += "%(name)s: %(points)s<br>" % {"name": name, "points": points}
    return render_template('points.html', points = lines)