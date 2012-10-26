from inspire import app, db
from config import visible, public_name, internal_name, blueprint
from flask import Flask, request, flash, redirect, url_for, render_template, g, session
                        
@blueprint.route('/')
@app.inspire
def index():
    return render_template(internal_name + '/index.html')
    