# Just load all the python files in this directory
import os
dir = os.listdir(os.path.dirname(__file__))
for d in dir:
    if d[-3:] == '.py' and d[0] != '_':
        __import__("inspire.web." + d[:-3], fromlist = ["*"])