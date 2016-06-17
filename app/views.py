from app import lm,db,app
from flask import render_template,redirect,url_for,flash,request,jsonify
from flask_login import login_required,current_user,login_user,logout_user
from .models import User,Post
from .forms import LoginForm,RegisterForm,PostForm
from .exceptions import InvalidUsage

import time


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('index',user=user.username))
        else:
            flash('Invalid Login')
    return render_template('login.html',form=form)


@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Successful Registrations')
        return redirect(request.args.get('next'),url_for('login'))
    return render_template('signup.html',form=form)

@app.route('/<user>/index',methods=['GET','POST'])
@login_required
def index(user):
    if user != current_user.username:
        raise InvalidUsage(message='Unauthorized Access',status_code=411)
    user_obj = User.query.filter_by(username=user).first()
    posts = user_obj.posts.all()
    form = PostForm()
    print form.errors
    if form.validate_on_submit():
        post = Post(title=form.title.data,body=form.body.data,author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('post added')
        return redirect(url_for('.index',user=current_user.username))
    return render_template('index.html',user=user,posts=posts,form=form)

@app.route('/get/<user>',methods=['GET','POST'])
def getuser(user):
    u = User.query.filter_by(username=user).first()
    if u is not None:
        return jsonify(username=u.username,id=u.id)
    raise InvalidUsage(message='User does\'nt exist',status_code=404)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    app.logger.error('{0} ERROR:{1},{2}'.format(error.status_code,error.message,time.asctime(time.localtime(time.time()))))
    return response
