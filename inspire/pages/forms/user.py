from flask.ext.wtf import Form, TextField, PasswordField, validators

class LoginForm(Form):
    email = TextField('Email',
                         validators=[validators.Required(),
                                     validators.Length(min=1)])
    password = PasswordField('Password',
                         validators=[validators.Required(),
                                     validators.Length(max=50)])
                                     
class RegisterForm(Form):
    email = TextField('Email',
                        validators=[validators.Required(),
                                     validators.Length(min=1)])
    password = PasswordField('Password',
                        validators=[validators.Required(),
                                     validators.Length(max=50)])
    name = TextField('Name',
                        validators=[validators.Required(),
                                     validators.Length(min=3)])
