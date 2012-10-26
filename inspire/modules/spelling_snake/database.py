from inspire import app, db
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc
import passlib.hash
from inspire.lib.history_meta import Versioned

class Dogs(Versioned, db.Model):
    __tablename__ = 'spelling_snake_dogs'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #owner = db.relationship('User', backref=db.backref('user', lazy='joined'))
    
    def __repr__(self):
        return '<Dog %s>' % self.name
        
tables= [Dogs]
    
def populate_tables():
    print "Populating tables for Spelling Snake"
    
def upgrade_tables():
    print "Upgrading tables for Spelling Snake"