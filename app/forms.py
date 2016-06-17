from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField,ValidationError,TextAreaField
from wtforms.validators import DataRequired,Required,EqualTo
from .models import User

class LoginForm(Form):
    username = StringField('Enter Your Username',validators=[DataRequired()])
    password = PasswordField('Enter Your Password',validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(Form):
    username = StringField('Choose Your Username',validators=[DataRequired()])
    password = PasswordField('Chose Your Password',validators=[Required(),EqualTo('password_retype',message='Passwords Must Match')])
    password_retype = PasswordField('Retype Password',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists')

class PostForm(Form):
    title = StringField('Enter Title',validators=[DataRequired()])
    body = TextAreaField('write a post',validators=[DataRequired()])
    submit = SubmitField('Submit')
