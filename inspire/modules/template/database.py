from inspire import app, db
from inspire.database import User

from config import internal_name, safe_name

#Define Tables

# The Dictionary Table is a built-in table that you can safely remove if you
# don't need it.
class Dictionary(db.Model):
    __tablename__ = safe_name('dictionary')
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref(safe_name('dictionary_user_ref')))
    time_created = db.Column(db.DateTime)
    time_modified = db.Column(db.DateTime)
    teacher_id = db.Column(db.Integer)
    teacher = db.relationship('User', backref=db.backref(safe_name('dictionary_teacher_ref')))
    key = db.Column(db.String, unique = True)
    value = db.Column(db.String)

# List Table Names
tables = [Dictionary]
    
# Generate sample data for the table
def populate_tables():
    pass
    
# Code to migrate tables between the older version and new version
def upgrade_tables():
    pass
    