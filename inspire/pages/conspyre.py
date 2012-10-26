from inspire import app
from inspire.database import User
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session, jsonify

from inspire.conspyre_aux import json_success, json_error, check_request_arguments
    
@app.route('/test/<module>')
def test(module):
    if module in [a_module.internal_name for a_module in app.activity_modules]:
        return json_success()
    else:
        return json_error(message="Module not found!")
    
@app.route("/conspyre/login")
@app.route("/conspyre/login/")
def student_login():
    if check_request_arguments('email', 'password'):
        return json_error(message="You did not specify a username and/or password")
    email = request.args['email']
    password = request.args['password']
    user = User.query.filter(User.email == email).first()
    if user is None:
        return json_error(message="User not found")
    if not user.verify_password(password):
        return json_error(message="User/Password mismatch")
    return json_success(name=user.name, id=user.id)
    
    
@app.route("/conspyre/get_type")
@app.conspyre()
def conspyre_get_type():
    return json_success(type=g.user.user_type)