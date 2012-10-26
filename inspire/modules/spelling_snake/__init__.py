from inspire import app, db
from flask import Flask, request, flash, redirect, url_for, render_template, g, session

from database import populate_tables, upgrade_tables
    
from config import visible, public_name, internal_name, blueprint
                        
@blueprint.route('/')
@app.inspire
def index():
    return render_template('spelling_snake/index.html')
    
@app.conspyre()
def get_word_list():
    pass
@app.conspyre()
def buy_outfit(outfit, points_spent):
    pass
@app.conspyre()
def save_progress(level_completion_speed, level_errors, points_gained):
    pass
@app.conspyre()
def load_progress():
    pass
