from inspire import app, db
from config import visible, public_name, internal_name, blueprint, safe_name
from flask import Flask, request, flash, redirect
from flask import url_for, render_template, g, session

from inspire.main_database import User
from database import TemplateDictionary


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

@blueprint.route('/points')
@blueprint.route('/points/')
@app.inspire
def view_points():
    dictionary_query = TemplateDictionary.query.filter(TemplateDictionary.key == 'points').all()
    lines = []
    for dictionary in dictionary_query:
        name = "%s" % dictionary.user.name
        points = dictionary.value
        lines.append("%(name)s: %(points)s" % {"name": name, "points": points})
    return render_template(internal_name+'/points.html', lines = lines)