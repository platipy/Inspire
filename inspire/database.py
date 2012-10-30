# This file really needs a better name. We'll discuss later
from inspire import db
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc
import passlib.hash
from inspire.lib.history_meta import Versioned

Reset_Requests = db.Table('Reset_Requests', db.Model.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('teacher_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('approved', db.Boolean)
)

class User(Versioned, db.Model):
    user_types = ["guest","student","teacher","developer","admin"]
    GUEST, STUDENT, TEACHER, DEVELOPER, ADMIN = xrange(5)
    __tablename__ = 'user'

    @property
    def password(self):
        raise Exception("Plaintext passwords are not stored!")
        
    @password.setter
    def password(self, value):
        # TODO: Verify password strength somewhere
        self.pwhash = passlib.hash.sha512_crypt.encrypt(value)
        
    def verify_password(self, password):
        return passlib.hash.sha512_crypt.verify(password, self.pwhash)
        
    # Required information
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(40), unique = True, nullable = False)
    pwhash = db.Column(db.String(119), unique = False, nullable = False)
    name = db.Column(db.String(256), unique = False, nullable = False)
    user_type = db.Column(db.Integer)
    teacher_requesting = db.relationship('User',
                               secondary= Reset_Requests,
                               primaryjoin=Reset_Requests.c.student_id==id,
                               secondaryjoin=Reset_Requests.c.teacher_id==id,
                               backref = 'student_requesting')

    def __repr__(self):
        return '<User %s (%s)>' % (self.email, self.name)
               
def populate():
    u1 = User(email='acbart', password='pass', name='Austin Cory Bart', user_type=User.ADMIN)
    db.session.add(u1)
    u2 = User(email='lelouch', password='pass', name='Lelouch Lamperouge', user_type=User.STUDENT)
    db.session.add(u2)
    u3 = User(email='cookies', password='pass', name='Mr. Monster', user_type=User.TEACHER)
    db.session.add(u3)
    u4 = User(email='trex', password='pass', name='Rebecca Trexler', user_type=User.DEVELOPER)
    db.session.add(u4)
    
    db.session.flush()
    
    i = Reset_Requests.insert().values(student_id=u2.id, teacher_id=u1.id)
    db.session.execute(i)
    
    i = Reset_Requests.insert().values(student_id=u3.id, teacher_id=u1.id)
    db.session.execute(i)
    
    db.session.commit()
        
# class Prompt(Versioned, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    # prompt = db.Column(db.Text, nullable = False)
    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # author = db.relationship('User', backref=db.backref('user', lazy='joined'))
    
    # def __repr__(self):
        # return '<Prompt %d>' % self.id
    
    
# class Response(Versioned, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    # text = db.Column(db.Text)
    # prompt_id = db.Column(db.Integer, db.ForeignKey('prompt.id'))
    # author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # prompt = db.relationship('Prompt')
    # author = db.relationship('User')
    
    # def __repr__(self):
        # return '<Response %d>' % self.id