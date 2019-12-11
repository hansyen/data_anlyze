from builtins import dict

from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, current_user

from main.forms import LoginForm, ResetPasswordForm, RegistrationForm
from models import Role, BackEndUser, User
from __init__ import bcrypt, db, login_manager

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)

@main.context_processor  # 將class丟到前端
def inject_role():
    return dict(Role=Role)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(name=form.name.data, password=hashed_password, api_code=form.api_code.data)  #add new user, 要符合form
            db.session.add(user)    #寫入資料庫
            db.session.commit()
            
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('main.login'))
    except:
        flash('Your account name already used!', 'warning')
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  #對帳密
        user = User.query.filter_by(name=form.name.data).first()
        try:
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
            else:
                flash('Please check your account and password.', 'warning')
        except:
            flash('Please check your account and password.', 'warning')

    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/changeuserinfo', methods=['GET', 'POST'])   #重設密碼
def change_user_info():
    passwordform = ResetPasswordForm()
    if passwordform.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, passwordform.original_password.data):
            hashed_password = bcrypt.generate_password_hash(passwordform.password.data).decode('utf-8')
            current_user.password = hashed_password
            db.session.commit()
            flash('Reset password successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            return redirect(url_for('main.home'))
            flash('Current password is not correct', 'warning')
    form = LoginForm()
    name = current_user.name
    user = User.query.filter_by(name=name).first()
    return render_template('/changeuserinfo.html', user_info=user, form=form)