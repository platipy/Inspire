from flask import g

from inspire import app, db
from inspire.conspyre_aux import json_success, json_error, check_request_arguments
from config import blueprint

from database import User
from inspire.modules.example.database import Dog

@app.conspyre(blueprint)
def get_dog_list():
    dogs = []
    for dog in Dog.query.filter(Dog.owner == g.user).all():
        dogs.append({'name': dog.name, 'id': dog.id})
    return json_success(dogs = dogs)
    
@app.conspyre(blueprint)
def add_dog(breed, name):
    d = Dog(name = name, breed=breed, owner = g.user)
    db.session.add(d)
    db.session.commit()
    return json_success()
    
@app.conspyre(blueprint)
def release_dog(id):
    d = Dog.query.filter(Dog.id == id).first()
    db.session.delete(d)
    # Alternatively
    # Dog.query.filter(Dog.id==id).delete()
    db.session.commit()
    return json_success()

@app.conspyre(blueprint)    
def rename_dog(id, name):
    d = Dog.query.filter(Dog.id == id).first()
    d.name = name
    db.session.commit()
    return json_success()
    