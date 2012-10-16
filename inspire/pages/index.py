from inspire import app, g

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

@app.route('/')
def index():
    #print url_for("index")
    return render_template('index.html')
    