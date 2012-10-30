from inspire import app, db
from inspire.database import User, Reset_Requests
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
def _student_login():
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

@app.route('/conspyre/register')
@app.route("/conspyre/register/")
def _student_register():
    if check_request_arguments('email', 'password', 'name'):
        return json_error(message="You did not specify a username, name and/or password")
    email = request.args['email']
    password = request.args['password']
    name = request.args['name']
    if User.query.filter(User.email == email).count() > 0:
        return json_error(message="Username already in use")
    user = User(email=email, 
             password=password, 
             name=name, 
             user_type=User.STUDENT)
    db.session.add(user)
    db.session.commit()
    return json_success(id = user.id)
    
@app.route('/conspyre/request_reset')
@app.route("/conspyre/request_reset/")
def _student_request_reset():
    email = request.args['student']
    teacher_id = request.args['teacher']
    student = User.query.filter(User.email == email).first()
    Reset_Requests.insert().values(student = student, 
                                   teacher_id = teacher_id, 
                                   approved=False)
    db.session.commit()
    return json_success()
    
@app.route('/conspyre/teacher_list')
@app.route("/conspyre/teacher_list/")
def _student_teacher_list():
    teachers = User.query.filter(User.user_type == User.TEACHER).all()
    teachers = [{'id': teacher.id, 
                 'name': teacher.name}
                for teacher in teachers]
    return json_success(teachers= teachers)

@app.route('/conspyre/student_list')
@app.route("/conspyre/student_list/")
def _student_student_list():
    teacher_id = request.args['teacher']
    students = User.query.filter(User.user_type == User.STUDENT).all()
    students = list(set(student.name for student in students))
    return json_success(students= students)
    
@app.route("/conspyre/get_type")
@app.conspyre()
def conspyre_get_type():
    return json_success(type=g.user.user_type)
    