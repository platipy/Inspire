from inspire import app, db
from inspire.main_database import User
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from forms.user import RegisterForm

@app.route("/register", methods=['GET', 'POST'])
@app.route("/register/", methods=['GET', 'POST'])
@app.global_data
def register():
    form = RegisterForm()
    if form.is_submitted():
        if form.validate_on_submit():
            if User.query.filter(User.name == form.name.data).count() > 0:
                flash("That name is already in use, please choose a different name that students will recognize as you.")
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
    
@app.route('/developer/register', methods=['GET', 'POST'])
@app.route("/developer/register/", methods=['GET', 'POST'])
@app.global_data
def register():
    form = RegisterForm()
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
                              user_type=User.DEVELOPER)
            db.session.add(u)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for("index"))
        else:
            flash("There was an error with your submission")
            return render_template("register.html", form=form)
    return render_template("register.html", form=form)