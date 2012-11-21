from inspire import app, db
from config import visible, public_name, internal_name, blueprint
from flask import Flask, request, flash, redirect, url_for, render_template, g, session
                        
@blueprint.route('/')
@app.inspire
def index():
    return render_template('index.html')

@blueprint.route('/dogs')
@app.inspire
def dogs():
    return render_template('index.html')
    
@blueprint.route('/dogs/add')
@app.inspire
def add_dogs():
    return render_template('index.html')
    
@blueprint.route('/dogs/remove')
@app.inspire
def remove_dogs():
    return render_template('index.html')
    
@blueprint.route('/dogs/edit')
@app.inspire    
def edit_dogs():
    return render_template('index.html')