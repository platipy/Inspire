from inspire import app, db
from inspire.database import User, Reset_Requests
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session, jsonify
from forms.login import RegisterForm
from flask.ext.wtf import Form, TextField, HiddenField, validators
from werkzeug.datastructures import ImmutableMultiDict

@app.route("/request_reset", methods=['GET', 'POST'])
@app.route("/request_reset/", methods=['GET', 'POST'])
@app.global_data
def request_reset():
    form = TextField('Email',
                     validators=[validators.Required()])
    if form.is_submitted():
        if form.validate_on_submit():
            if User.query.filter(User.name == form.name.data).count() > 0:
                flash("That name is already in use, please choose a different name.")
                render_template("register.html", form=form)
            if User.query.filter(User.email == form.email.data).count() > 0:
                flash("That email is already in use. Are you already registered?")
                render_template("register.html", form=form)    
            u = User(email=form.email.data, 
                              password=form.password.data, 
                              name=form.name.data, 
                              user_type=User.TEACHER)
            db.session.add(u)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for("index"))
        else:
            flash("There was an error with your submission")
            return render_template("register.html", form=form)
    return render_template("register.html", form=form)
    
@app.route('/_reset_request', methods=['GET', 'POST'])
@app.route("/_reset_request/", methods=['GET', 'POST'])
@app.login_required
@app.global_data
def _reset_request():
    id = request.args.get('id', None, type=int)
    if id is not None:
        r = Reset_Requests.query.filter(Reset_Requests.student_id==id).all()
        for r in r:
            print r
            #r.approved = True
        db.session.commit()
        return jsonify(message="Password was reset!")
    return jsonify(message="Invalid ID given")
    
@app.route('/view_resets', methods=['GET', 'POST'])
@app.route("/view_resets/", methods=['GET', 'POST'])
@app.login_required
@app.global_data
def view_resets():
    reset_requests = db.session.query(User.id, User.name).filter(User.teacher_requesting == g.user.id))
    reset_requests= [{'id' : r[0], 'name' : r[1]} for r in 
                        db.session.execute(reset_requests).fetchall()]
    return render_template("request.html", resets=reset_requests)
        
    # form = RegisterForm()
    # if form.is_submitted():
        # if form.validate_on_submit():
            # if User.query.filter(User.name == form.name.data).count() > 0:
                # flash("That name is already in use, please choose a different name.")
                # render_template("register.html", form=form)
            # if User.query.filter(User.email == form.email.data).count() > 0:
                # flash("That email is already in use. Are you already registered?")
                # render_template("register.html", form=form)    
            # u = User(email=form.email.data, 
                              # password=form.password.data, 
                              # name=form.name.data, 
                              # user_type=User.DEVELOPER)
            # db.session.add(u)
            # db.session.commit()
            # flash('Registration successful!')
            # return redirect(url_for("index"))
        # else:
            # flash("There was an error with your submission")
            # return render_template("register.html", form=form)
    # return render_template("register.html", form=form)