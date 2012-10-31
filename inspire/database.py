# This file really needs a better name. We'll discuss later
from inspire import db
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc
import passlib.hash
from inspire.lib.history_meta import Versioned


class Reset_Requests(db.Model):
    __tablename__ = 'reset_requests'
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    approved = db.Column(db.Boolean)
    
    students = db.relationship("User", 
                              backref='student_requesting',
                              primaryjoin="User.id == Reset_Requests.student_id")
    teachers = db.relationship("User", 
                              backref='teacher_requesting',
                              primaryjoin="User.id == Reset_Requests.teacher_id")
    
    def __repr__(self):
        return '<Request from %s to %s>' % (self.student_id, self.teacher_id)

class User(db.Model):
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
    
    r= Reset_Requests(student_id=u2.id, teacher_id=u1.id, approved=False)
    db.session.add(r)
    
    r= Reset_Requests(student_id=u3.id, teacher_id=u1.id, approved=True)
    db.session.add(r)
    
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