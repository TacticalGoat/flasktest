from app import db,bcrypt
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password_hash = db.Column(db.String(30))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a gettable property')

    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    body = db.Column(db.String,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %s>' % self.title
