from flask import g

from inspire import app, db
from inspire.conspyre_aux import json_success, json_error, check_request_arguments
from config import blueprint

from database import User
from inspire.modules.template.database import Dictionary
import datetime

@app.conspyre(blueprint)
def get(key):
    if Dictionary.query.filter(Dictionary.key == key, Dictionary.user == g.user).count() > 0:
        value= Dictionary.query.filter(Dictionary.key == key, 
                                       Dictionary.user == g.user).first()
        return json_success(value=value.value)
    else:
        return json_error(error="ValueNotFound")

@app.conspyre(blueprint)
def put(key, value):
    if Dictionary.query.filter(Dictionary.key == key, Dictionary.user == g.user).count() > 0:
        d = Dictionary.query.filter(Dictionary.key == key, 
                                    Dictionary.user == g.user).first()
        d.value = value
        d.time_modified = datetime.datetime.now()
        db.session.commit()
        return json_success()
    else:
        d= Dictionary(user = g.user, 
                   teacher_id= g.metadata['teacher'],
                   time_created = datetime.datetime.now(),
                   time_modified = datetime.datetime.now(),
                   key = key,
                   value = value)
        db.session.add(d)
        db.session.commit()
        return json_success()
    
@app.conspyre(blueprint)
def update(pairs):
    for key, value in pairs.items():
        if Dictionary.query.filter(Dictionary.key == key, Dictionary.user == g.user).count() > 0:
            d = Dictionary.query.filter(Dictionary.key == key, 
                                        Dictionary.user == g.user).first()
            d.value = value
            d.time_modified = datetime.datetime.now()
        else:
            d= Dictionary(user = g.user, 
                       teacher_id= g.metadata['teacher'],
                       time_created = datetime.datetime.now(),
                       time_modified = datetime.datetime.now(),
                       key = key,
                       value = value)
            db.session.add(d)
    db.session.commit()
    return json_success()
    
    
@app.conspyre(blueprint)
def has(key):
    query = Dictionary.query.filter(Dictionary.key == key, Dictionary.user == g.user).count()
    return json_success(has=query > 0)
    
