# This file really needs a better name. We'll discuss later
from inspire import db, config
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc
from datetime import datetime

#class Module(db.Model):
#    __tablename__ = 'modules'
    
    
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement= True)
    name = db.Column(db.String(30), unique = True, nullable = False)    
    email = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(30), unique = False, nullable = False)    
    type = db.Column(db.Enum("student","teacher","developer","guest", name="user_types"), nullable = False)
    
    def __init__(self, email, name, password, type):
        self.email = email
        self.name = name
        self.password = password
        self.type = type
        
    def __repr__(self):
        return '<User %s>' % self.email
        
    def verify_password(self, password):
        return self.password == password
        
        
user = User("acbart@udel.edu", "Mr. Bart", "password", "developer")
print str(user)