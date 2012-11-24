import traceback

from inspire import app, db
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from inspire.pages.admin import admin
from flask.ext.admin.contrib.sqlamodel import ModelView

# Try and load all the modules in modules/
import os
module_directories = os.listdir(os.path.dirname('inspire/modules/'))
modules = []

for d in module_directories:
    s = os.path.abspath("inspire/modules/") + os.sep + d
    if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):
        try:
            module = __import__("inspire.modules."+d, fromlist = ["*"])
            if hasattr(module, 'internal_name') and hasattr(module, 'public_name'):
                module._index_path = module.internal_name + '.index'
                app.register_blueprint(module.blueprint, 
                                       url_prefix='/modules/'+module.internal_name)
                if hasattr(module, 'tables'):
                    for a_table in module.tables:
                        print "Loading Model for %s." % d
                        admin.add_view(ModelView(a_table, db.session, category=d))
                modules.append(module)
                print "Loaded %s" % d
        except ImportError, e:
            traceback.print_exc()
        except:
            traceback.print_exc()
            
app.activity_modules = modules