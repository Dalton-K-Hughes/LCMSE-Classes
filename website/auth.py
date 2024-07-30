import os
from dotenv import load_dotenv
from flask import Blueprint, flash, redirect, render_template, request, url_for
import flask
from . import db
from .models import User
from .forms import LoginForm, SignUpForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
load_dotenv()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.user_name.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Login Successful!')
            next = flask.request.args.get('next')
            return redirect(url_for())
        else:
            flash('Invalid username or password!')
            return redirect(url_for('auth.login'))
        
    return render_template('login.html', form=form)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate():
        existingUser = User.query.filter_by(user_name=form.user_name.data).first()
        if existingUser:
            flash('Username already exists! Please Choose another username.', 'error')
            return render_template('sign-up.html', form=form)
        user = User(username=form.user_name.data, password=generate_password_hash(form.password.data), classSection=form.classChoice.data, admin=True if form.adminPassword.data == os.getenv('ADMIN_PASSWORD') else False)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registering!')
        return redirect(url_for('login.html'))
    
    return render_template('sign-up.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!')
    return redirect(url_for('auth.login')) 
        

