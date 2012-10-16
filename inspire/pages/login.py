from inspire import app, db, database
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, request, flash, redirect, url_for, render_template
from flask import session, g
from werkzeug.datastructures import ImmutableMultiDict

import pprint
pp = pprint.PrettyPrinter(indent=4)

import hashlib

                                     
def render_error():
    return render_template("login.html", error="Wrong username or password.")

@app.route("/register/<type>", methods=['GET', 'POST'])
@app.route("/teacher/register/", methods=['GET', 'POST'])
def register():
    return render_template("register.html", registration_type="Teacher")
    
@app.route("/reset_password")
@app.route("/reset_password/")
def reset_password():
    return "Reseting password" + str(dir(session))
    
@app.route("/teacher/login", methods=['GET', 'POST'])
@app.route("/developer/login", methods=['GET', 'POST'])
@app.route("/teacher/login/", methods=['GET', 'POST'])
@app.route("/developer/login/", methods=['GET', 'POST'])
def login():
    if 'submit' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = database.User.query.filter_by(email=email).first()
        print user, dir(user)
        if user is None:
            return render_template("login.html", error="The email wasn't found. Have you registered?")
        if not user.verify_password(password):
            return render_template("login.html", error="Password was incorrect.")
        flash("Login succesful.")
        session['username'] = email
        return redirect(url_for("index"))
    return render_template("login.html")
