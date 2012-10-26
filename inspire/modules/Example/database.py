from inspire import app, db
from inspire.database import User
from inspire.lib.history_meta import Versioned

from config import internal_name

class Dog(Versioned, db.Model):
    __tablename__ = internal_name + '_dog'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    breed = db.Column(db.String, nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('userDog', lazy='joined'))
    
    def __repr__(self):
        return '<Dog %s>' % self.name
        
class Points(Versioned, db.Model):
    __tablename__ = internal_name + '_points'
    value = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    player = db.relationship('User', backref=db.backref('userPoints', lazy='joined'))
    
    def __repr__(self):
        return '<%s points: %d>' % (self.name, self.value)
    
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
    
def upgrade_tables():
    pass
    