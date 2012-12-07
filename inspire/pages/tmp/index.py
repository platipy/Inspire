from accounts import app
from flask import render_template
from forms import LoginForm

@app.route('/')
def index():
    g.forms = {}
    g.forms['login'] = LoginForm
    return render_template('index.html')
