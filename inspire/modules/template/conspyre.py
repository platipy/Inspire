from flask import g

from inspire import app, db
from inspire.conspyre_aux import json_success, json_error, check_request_arguments
from config import blueprint

from inspire.main_database import User
from database import TemplateDictionary
import datetime

# Conspyre functions should look like:
#@app.conspyre(blueprint)
#def <method_name>(<arg1>, <arg2>, <arg3>, ...):
#   ... g.user ...
#   ... User.query ...
#   return json_success(key=value, key=value)
#   return json_error(error="ExceptionName")


@app.conspyre(blueprint)
def get(key):
    dictionary_query = TemplateDictionary.query.filter(TemplateDictionary.key == key, 
                                               TemplateDictionary.user == g.user)
    if dictionary_query.count() > 0:
        value= dictionary_query.first()
        return json_success(value.value)
    else:
        return json_error(error="ValueNotFound")
        
@app.conspyre(blueprint)
def items():
    items = TemplateDictionary.query.filter(TemplateDictionary.user == g.user).all()
    return json_success(dict([(item.key, item.value) for item in items]))
    
@app.conspyre(blueprint)
def put(key, value):
    dictionary_query = TemplateDictionary.query.filter(TemplateDictionary.key == key, 
                                               TemplateDictionary.user == g.user)
    if dictionary_query.count() > 0:
        d = dictionary_query.first()
        d.value = value
        d.time_modified = datetime.datetime.now()
    else:
        db.session.add(TemplateDictionary(user = g.user, 
                                  teacher_id= g.metadata['teacher'],
                                  time_created = datetime.datetime.now(),
                                  time_modified = datetime.datetime.now(),
                                  key = key,
                                  value = value))
    db.session.commit()
    return json_success()
    
@app.conspyre(blueprint)
def update(dict):
    for key, value in dict.items():
        dictionary_query = TemplateDictionary.query.filter(TemplateDictionary.key == key, 
                                                   TemplateDictionary.user == g.user)
        if dictionary_query.count() > 0:
            d = dictionary_query.first()
            d.value = value
            d.time_modified = datetime.datetime.now()
        else:
            db.session.add(TemplateDictionary(user = g.user, 
                                      teacher_id= g.metadata['teacher'],
                                      time_created = datetime.datetime.now(),
                                      time_modified = datetime.datetime.now(),
                                      key = key,
                                      value = value))
    db.session.commit()
    return json_success()
    
    
@app.conspyre(blueprint)
def has(key):
    dictionary_query = TemplateDictionary.query.filter(TemplateDictionary.key == key, 
                                               TemplateDictionary.user == g.user)
    return json_success((dictionary_query.count() > 0))
    
