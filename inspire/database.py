# This file really needs a better name. We'll discuss later
from inspire import db, config
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc
import passlib.hash
from inspire.lib.history_meta import Versioned


class User(Versioned, db.Model):
    user_types = ["guest","student","teacher","developer","admin"]
    GUEST, STUDENT, TEACHER, DEVELOPER, ADMIN = xrange(5)

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
    name = db.Column(db.String(256), unique = True, nullable = False)
    user_type = db.Column(db.Integer)

    def __repr__(self):
        return '<User %s (%s)>' % (self.email, self.name)
        
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