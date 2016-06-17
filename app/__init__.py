import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.login_view = 'login'
lm.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app import views,models