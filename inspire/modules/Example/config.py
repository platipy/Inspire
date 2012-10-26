from flask import Blueprint

# Change These
visible = True
public_name = "Example Game"
internal_name = "example"

# Keep this
blueprint = Blueprint(internal_name, 'inspire.modules.'+internal_name,
                      template_folder='templates',
                      static_folder='example/static')