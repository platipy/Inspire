htpath = '.'
db_type = 'mysql'

sqlite_file = 'db.sqlite'

mysql = {}
mysql['user']    = 'conspyre'
mysql['pass']    = 'not_password'
mysql['host']    = 'localhost'
mysql['port']    = '3306'
mysql['db']      = 'conspyre'
mysql['charset'] = 'utf8'
mysql['driver']  = 'pymysql'

# These should only be changed during development
# Any of these being true in production is an security vulnerability which is
# beyond trivial to exploit. Don't leave these on, ever.
flask_secret_key = "dev_key"
flask_debug = True
flask_test = False
dev_port = 5000
class FlaskConfig():
    DEBUG = flask_debug
    TESTING = flask_test
    SECRET_KEY = flask_secret_key
    SQLALCHEMY_DATABASE_URI = 'mysql+%(driver)s://%(user)s:%(pass)s@%(host)s:%(port)s/%(db)s?charset=%(charset)s' % mysql