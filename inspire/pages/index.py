from inspire import app
from inspire.main_database import *

from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from forms.login import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/index/')
@app.route('/modules')
@app.route('/modules/')
@app.login_required
@app.global_data
def index():
    return render_template('index.html')
