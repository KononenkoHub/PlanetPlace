from flask import render_template, request, redirect, url_for
from models import User, Test
from forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user, current_user
from main import login, app, db, APP_ROOT
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    print('user status - ', current_user.is_authenticated)
    return render_template('index.html', user_authenticated=current_user.is_authenticated)


@app.route('/user')
@login_required
def user():
    return render_template('user.html', user=current_user.username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password_hash,form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
        return 'We can`t find this user. Please registr on this site'
    return render_template('login.html', title='Login', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        target = os.path.join(APP_ROOT, 'static/avatars/')
        if not os.path.isdir(target):
            os.makedirs(target)

        file = request.files['file']
        filename = secure_filename(file.filename)
        destination = '/'.join([target, filename])
        file.save(destination)
        '''
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        planet=form.planet.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        '''
        new_user = Test(username=form.username.data,
                        email=form.email.data,
                        planet=form.planet.data,
                        avatar=file.read(),
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        print(f'Account created for {form.username.data}!', 'success')

        return redirect(url_for('user', name=form.username.data))
    return render_template('register.html', title='Register', form=form)


@app.route('/infoforguest')
def info():
    return render_template('infoforguest.html')


@app.route('/infoforusers')
def info_for_user():
    return render_template('infoforusers.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
