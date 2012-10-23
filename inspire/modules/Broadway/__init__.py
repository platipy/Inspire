from flask import Blueprint, render_template, abort

simple_page = Blueprint('broadway', __name__,
                        template_folder='templates')

print "Found Broadway"

def create_tables():
    print "Creating tables for Broadway"
    
def delete_tables():
    print "Deleting tables for Broadway"
    
def populate_tables():
    print "Populating tables for Broadway"
    
def upgrade_tables():
    print "Upgrading tables for Broadway"
    
name = "Broadway"
internal_name = "broadway"

