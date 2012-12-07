import os, sys
import time
from inspire import app, db
from inspire.main_database import User, Reset_Requests
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session, jsonify
import json

from inspire.conspyre_aux import json_success, json_error
    
@app.route('/test/<module>')
def test(module):
    if module in [a_module.internal_name for a_module in app.activity_modules]:
        return json_success()
    else:
        module_dir= 'inspire/modules'
        new_module= os.path.join(module_dir, module)
        if os.path.exists(module_dir) and not os.path.exists(new_module):
            os.makedirs(new_module)
            # Log File
            f = open(os.path.join(new_module, 'log.txt'), 'w')
            f.write("Module automatically created at %s.\n" % (time.ctime(float(time.time())),))
            f.close()
            # Init File
            f = open(os.path.join(new_module, '__init__.py'), 'w')
            f.write("")
            f.close()
            return json_success()
        return json_error(error="ModuleNotFound")

@app.route('/logging/<module>', methods=['POST'])
def _logging(module):
    log_file = 'inspire/modules/%s/log.txt' % (module,)
    if os.path.exists(log_file):
        f = open(log_file, 'a')
        artifact = json.loads(request.data)
        entry = "%(message)s\n\t%(time)s\n" % {"time" : time.ctime(float(artifact['metadata']['time'])),
                   "message": artifact['message']}
        if artifact['metadata']['email']:
            entry+= ("\tUser: %(email)s (%(id)d)\n" % 
                    {"email" : artifact['metadata']['email'],
                     "id" : artifact['metadata']['id']})
        if artifact['metadata']['teacher']:
            entry+= ("\tTeacher: %(teacher)s\n" % 
                     {"teacher" : artifact['metadata']['teacher']})
        f.write(entry)
        f.close()
        return json_success()
    else:
        return json_error(error="FailedToSaveLog")
    
@app.route("/conspyre/login")
@app.route("/conspyre/login/")
def _student_login():
    email = request.args['email']
    password = request.args['password']
    user = User.query.filter(User.email == email).first()
    if user is None:
        return json_error(error="UserNotFound")
    if not user.verify_password(password):
        return json_error(error="PasswordMismatch")
    return json_success(name=user.name, id=user.id)

@app.route('/conspyre/register')
@app.route("/conspyre/register/")
def _student_register():
    email = request.args['email']
    password = request.args['password']
    name = request.args['name']
    if User.query.filter(User.email == email).count() > 0:
        return json_error(error="UsernameExists")
    user = User(email=email, 
             password=password, 
             name=name, 
             user_type=User.STUDENT)
    db.session.add(user)
    db.session.commit()
    if 'teacher' in request.args:
        teaching = Teaching(student= user,
                            teacher_id= request.args['teacher'],
                            time= time.time())
        db.session.add(teaching)
        db.session.commit()
    return json_success(id = user.id)
    
@app.route("/conspyre/reset_password")
@app.route("/conspyre/reset_password/")
def _student_reset_password():
    email = request.args['email']
    password = request.args['password']
    user = User.query.filter(User.email == email).first()
    if user is None:
        return json_error(error="UserNotFound")
    reqs = Reset_Requests.query.filter(Reset_Requests.student_id==user.id).all()
    if not any(r.approved for r in reqs):
        return json_error(error="ResetNotApproved")
    user.password = password
    db.session.commit()
    return json_success(name=user.name, id=user.id)
    
@app.route('/conspyre/password_resetable')
@app.route("/conspyre/password_resetable/")
def _student_password_resetable():
    email = request.args['student']
    student = User.query.filter(User.email == email).first()
    reqs = Reset_Requests.query.filter(Reset_Requests.student_id==student.id).all()
    return json_success(status=not any(r.approved for r in reqs))
    
@app.route('/conspyre/request_reset')
@app.route("/conspyre/request_reset/")
def _student_request_reset():
    email = request.args['student']
    teacher_email = request.args['teacher']
    student = User.query.filter(User.email == email).first()
    teacher = User.query.filter(User.email == teacher_email).first()
    if Reset_Requests.query.filter(Reset_Requests.student_id==student.id).count() == 0:
        r = Reset_Requests(student_id = student.id, 
                        teacher_id = teacher.id, 
                        approved=False)
        db.session.add(r)
        db.session.commit()
        return json_success()
    return json_error(error="ResetAlreadyRequested")
    
@app.route('/conspyre/teacher_list')
@app.route("/conspyre/teacher_list/")
def _student_teacher_list():
    teachers = User.query.filter(User.user_type == User.TEACHER).all()
    teachers = [{'id': teacher.id, 
                 'name': teacher.name,
                 'username': teacher.email}
                for teacher in teachers]
    return json_success(teachers= teachers)

@app.route('/conspyre/student_list')
@app.route("/conspyre/student_list/")
def _student_student_list():
    teacher_id = request.args['teacher']
    if not teacher_id:
        students = User.query.filter(User.user_type == User.STUDENT).all()
        students = [{'name': student.name, 
                     'id'  : student.id, 
                     'username': student.email} for student in students]
        return json_success(students= students)
    else:
        students = User.query.filter(User.user_type == User.STUDENT).all()
        students = [{'name': student.name, 
                     'id'  : student.id, 
                     'username': student.email} for student in students]
        return json_success(students= students)
    
@app.route("/conspyre/get_type")
@app.conspyre()
def conspyre_get_type():
    return json_success(type=g.user.user_type)
    