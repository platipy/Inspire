import traceback

from inspire import app
from flask import Flask, request, flash, redirect, url_for, render_template, g
from flask import session
from inspire.database import *

# Try and load all the modules in modules/
import os
module_directories = os.listdir(os.path.dirname('inspire/modules/'))
modules = []

for d in module_directories:
    s = os.path.abspath("inspire/modules/") + os.sep + d
    if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):
        try:
            module = __import__("inspire.modules."+d, fromlist = ["*"])
            modules.append(module)
            print "Loaded %s" % d
        except ImportError, e:
            traceback.print_exc()
        except:
            traceback.print_exc()
            
app.activity_modules = modules