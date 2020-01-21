from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import os

APP_ROOT = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login = LoginManager()
login.init_app(app)
login.login_view = 'login'

from views import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
