from inspire import app
from flask import session, flash, redirect, url_for

@app.route('/logout')
@app.route('/logout/')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('index'))