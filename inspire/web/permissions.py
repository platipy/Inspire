from flask import session, g, redirect, url_for, flash, request
from inspire.database import User
from inspire import app, db, config
from decorator import decorator
from functools import wraps

import json
import fix_json

from inspire.conspyre_aux import json_success, json_error, check_request_arguments

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
    
@decorator
def inspire(f, *args, **kwargs):
    g.modules = app.activity_modules
    if 'uid' in session:
        u = User.query.filter(User.id == session['uid']).first()
        g.user = u
        return f(*args, **kwargs)
    else:
        g.user= None
        flash("You are not logged in yet.")
        return redirect(url_for('login'))
    
def conspyre(blueprint=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            artifact = json.loads(request.data)
            id = artifact['metadata']['id']
            password = artifact['metadata']['password']
            user = User.query.filter(User.id == id).first()
            if user is None:
                return json_error(message="Failed to perform %s. User not found" % f.__name__)
            if not user.verify_password(password):
                return json_error(message="Failed to perform %s. User/Password mismatch" % f.__name__)
            g.user = user
            g.metadata = artifact['metadata']
            kwargs.update(artifact['data'])
            return f(*args, **kwargs)
        if blueprint is not None:
            blueprint.add_url_rule('/'+f.__name__, f.__name__, decorated_function, methods=['POST'])
        return decorated_function
    return decorator

app.login_required = login_required
app.global_data = global_data
app.inspire = inspire
app.conspyre = conspyre