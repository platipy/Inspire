# boilerplate to allow running as script directly
if __name__ == "__main__" and __package__ is None or __package__ == '':
    import sys, os
    # The following assumes the script is in the top level of the package
    # directory.  We use dirname() to help get the parent directory to add to
    # sys.path, so that we can import the current package.  This is necessary 
    # since when invoked directly, the 'current' package is not automatically
    # imported.
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    sys.path.insert(0, os.path.abspath("inspire/lib"))
    import lib
    import inspire
    inspire.main()
    
    
# Low Level imports
# from optparse import OptionParser

# from inspire import app

# parser = OptionParser()
# parser.add_option("-s", "--server", dest="local", default=True,
                  # action="store_false",
                  # help="Run as server (mickey.cs.vt.edu:8222 currently)")
# parser.add_option("-l", "--local", dest="local",
                  # action="store_true", default=True,
                  # help="Run locally (127.0.0.1:5000)")

# (options, args) = parser.parse_args()
# if options.local:
    # app.run(host='127.0.0.1', port=5000)
# else:
    # app.run(host='mickey.cs.vt.edu', port=8222)
