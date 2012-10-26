from flask import Blueprint, render_template, abort
from inspire import app, db
from flask import Flask, request, flash, redirect, url_for, render_template, g, session

def create_tables():
    print "Creating tables for Broadway"
    
def delete_tables():
    print "Deleting tables for Broadway"
    
def populate_tables():
    print "Populating tables for Broadway"
    
def upgrade_tables():
    print "Upgrading tables for Broadway"
    
visible = True
public_name = "Broadway"
internal_name = "broadway"
blueprint = Blueprint('broadway', 'broadway',
                        template_folder='templates',
                        static_folder='static')
                        
@blueprint.route('/')
@app.inspire
def index():
    return g.user.name + " is welcomed"
    
@app.conspyre()
def get_teacher_image():
    pass
@app.conspyre()
def get_wip_story():
    pass
@app.conspyre()
def save_wip_story():
    pass
@app.conspyre()
def publish_story():
    pass