import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import basedir

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.login_view = 'login'
lm.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
handler = RotatingFileHandler('test.log',maxBytes=10000,backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

from app import views,models
