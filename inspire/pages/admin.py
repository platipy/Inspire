from inspire import app, db
from inspire.database import *
from flask.ext.admin import Admin, BaseView, expose, AdminIndexView
from flask import request, g
from flask.ext.admin.contrib.sqlamodel import ModelView

class AdminIndex(AdminIndexView):
    #@app.setup
    def is_accessible(self):
        print g.user
        return g.user is not None and g.user.username == 'admin'
    
    #@app.setup
    @expose('/')
    def index(self):
        return self.render('admin/index.html')
        
admin = Admin(app, name='Inspire', index_view = AdminIndex())
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(User.__history_mapper__.class_, db.session))
#admin.add_view(ModelView(Prompt, db.session))
#admin.add_view(ModelView(Response, db.session))