from inspire import app
from inspire.main_database import User
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session

@app.route("/logout", methods=['GET', 'POST'])
@app.route("/logout/", methods=['GET', 'POST'])
@app.global_data
def logout():
    g.user = None
    session.pop('uid', None)
    flash("You were logged out")
    return redirect(url_for('login'))