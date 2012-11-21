from inspire import app, db
from inspire.database import User
from inspire.lib.history_meta import Versioned

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

class Dog(Versioned, db.Model):
    __tablename__ = safe_name('dog')
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    breed = db.Column(db.String, nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref(safe_name('dog_ref')))
    
    def __repr__(self):
        return '<Dog %s>' % self.name
        
class Points(Versioned, db.Model):
    __tablename__ = safe_name('points')
    value = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    player = db.relationship('User', backref=db.backref(safe_name('points_ref')))
    
    def __repr__(self):
        return '<%s points: %d>' % (self.name, self.value)
    
# List Table Names
tables = [Dictionary, Dog, Points]
    
# Generate sample data for the table
def populate_tables():
    u = User(email='dog_lover', password='pass', name='Kyle', user_type=User.STUDENT)
    db.session.add(u)
    db.session.flush()
    
    d = Dog(name = "Fido", breed="Black Lab", owner = u)
    db.session.add(d)
    d = Dog(name = "Ada", breed="Corgi")
    db.session.add(d)
    
    p = Points(player = u, value = 0)
    db.session.add(p)
    
    db.session.commit()
    
# Code to migrate tables between the older version and new version
def upgrade_tables():
    pass
    