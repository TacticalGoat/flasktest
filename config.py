import os

WTF_CSRF_TOKEN = True
SECRET_KEY = 'Damien-Sandow'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'test.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repositrory')
