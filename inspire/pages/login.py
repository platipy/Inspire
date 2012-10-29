from inspire import app
from inspire.database import User
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from forms.user import LoginForm

@app.route("/login", methods=['GET', 'POST'])
@app.route("/login/", methods=['GET', 'POST'])
@app.global_data
def login():
    form = LoginForm()
    if form.is_submitted():
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()
            if user is None:
                # User doesn't exist!
                flash("That email is not associated with a user.")
                return render_template('index.html', form=form)
            if not user.verify_password(form.password.data):
                # Password is wrong!
                flash("The password and email combination was not found.")
                return render_template('index.html', form=form)
            session['uid'] = user.id
            g.user = user
            flash('Thanks for logging in, %s' % user.name)
            return redirect(url_for('index'))
        else:
            # Some deeper problem in submission
            flash("There was an error logging in. Please try again.")
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)