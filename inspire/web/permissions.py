from flask import session, g, redirect, url_for, flash
from inspire.database import User
from inspire import app, db, config
from decorator import decorator
from functools import wraps

#TODO: Mix this in with route decorator
@decorator
def login_required(f, *args, **kwargs):
    if 'uid' in session:
        u = User.query.filter(User.id == session['uid']).first()
        g.user = u
        return f(*args, **kwargs)
    else:
        g.user= None
        flash("You are not logged in yet.")
        return redirect(url_for('login'))
        
@decorator
def global_data(f, *args, **kwargs):
    g.modules = app.activity_modules
    return f(*args, **kwargs)
    
app.login_required = login_required
app.global_data = global_data