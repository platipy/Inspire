from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from optparse import OptionParser
import sys
import config
import unittest
import dataset
#from inspire.lib.history_meta import versioned_session

try:
    from . import config
except ImportError:
    print "Configuration file missing. See README for details on configuration."
    exit(-1)
    
def main():
    global app, db, web, database, pages
    parser = OptionParser()
    parser.add_option("-r", "--reset-db", action="store_true", default=False, dest="reset_db", help="Reset the database.")
    parser.add_option("--server",  action="store_true", default=False, dest="start_server", help="Run the test webserver.")
    (options, args) = parser.parse_args()
    
    import hacks
    
    if options.reset_db or options.start_server:
        # Setup the application and database
        app = Flask(__name__.split('.')[0])
        app.config.from_object(config.FlaskConfig)
        app.jinja_env.add_extension('jinja2.ext.do')
        db = SQLAlchemy(app)
        #versioned_session(db.session)
        import database
        import web
        if options.reset_db:
            db.drop_all()
            db.create_all()
            dataset.populate()
            print 'Database reset.'
            #exit(0)
        import pages
        import module_loader
        app.run(host='0.0.0.0', port=config.dev_port, use_reloader=True)
    else:
        parser.print_help()
        
def wsgi():
    global app, db, web, database, pages
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config.FlaskConfig)
    app.jinja_env.add_extension('jinja2.ext.do')
    db = SQLAlchemy(app)
    import database
    import web
    import pages