from flask import Blueprint

# Change These
visible = False
internal_name = "!@#$%^template!@#$%^"
public_name = "!@#$%^PUBLIC_TEMPLATE!@#$%^"

# Keep this
def safe_name(name):
    return "%s_%s" % (internal_name, name)

blueprint = Blueprint(internal_name, 'inspire.modules.'+internal_name,
                      template_folder=internal_name+'/templates',
                      static_folder= internal_name+'/static')