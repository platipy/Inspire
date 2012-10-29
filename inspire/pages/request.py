from inspire import app, db
from inspire.database import User, Reset_Requests
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from forms.login import RegisterForm
from flask.ext.wtf import Form, TextField, HiddenField, validators

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
    
@app.route('/view_resets', methods=['GET', 'POST'])
@app.route("/view_resets/", methods=['GET', 'POST'])
@app.login_required
@app.global_data
def view_resets():
    reset_requests = db.session.query(User.id, 
                                      User.name).filter(User.teacher_requesting.any(id=g.user.id))
    reset_requests= db.session.execute(reset_requests).fetchall()
    
    forms = [(TextField(a_request[1]), HiddenField(a_request[0])) 
                for a_request in reset_requests]
    return render_template("request.html", forms=forms)
        
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