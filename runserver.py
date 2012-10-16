# Low Level imports
from optparse import OptionParser

from inspire import app

parser = OptionParser()
parser.add_option("-s", "--server", dest="local", default=True,
                  action="store_false",
                  help="Run as server (mickey.cs.vt.edu:8222 currently)")
parser.add_option("-l", "--local", dest="local",
                  action="store_true", default=True,
                  help="Run locally (127.0.0.1:5000)")

(options, args) = parser.parse_args()
if options.local:
    app.run(host='127.0.0.1', port=5000)
else:
    app.run(host='mickey.cs.vt.edu', port=8222)
