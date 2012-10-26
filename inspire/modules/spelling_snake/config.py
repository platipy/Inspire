from flask import Blueprint

visible = True
public_name = "Spelling Snake"
internal_name = "spelling_snake"
blueprint = Blueprint(internal_name, internal_name,
                      template_folder='templates',
                      static_folder='static')