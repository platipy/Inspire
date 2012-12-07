from flask import Blueprint

# Change These
visible = False
internal_name = "!!@@!!"
public_name = "!!@@!!"

# Keep this
def safe_name(name):
    return "%s_%s" % (internal_name, name)

blueprint = Blueprint(internal_name, 'inspire.modules.'+internal_name,
                      template_folder='templates',
                      static_folder=internal_name+'/static')