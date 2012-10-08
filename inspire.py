from __future__ import with_statement

# Import database call
#import sqlalchemy
import sqlite3
from contextlib import closing

# Flask stuff
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
     
# Configuration constants are in the config module
import config

# Actual app creation
app = Flask(__name__)
app.config.from_object(config)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
    
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
        
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
    
    
@app.route('/')
def show_entries():
    cur = g.db.execute('select username, visible_name from users order by username desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
    
    
if __name__ == '__main__':
    init_db()
    app.run()