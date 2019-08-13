from ytsearch.configs import db
from flask import flash, redirect, render_template, url_for, Blueprint
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash
from ytsearch.blueprints.forms.models import LoginForm, RegisterForm
from ytsearch.models import User

forms_bp = Blueprint('forms', __name__)


@forms_bp.route('/login', methods=['GET'])
def get_login_form():
    form = LoginForm()
    return render_template('forms/login.html', form=form)


@forms_bp.route('/login', methods=['POST'])
def submit_login_form():
    form = LoginForm()
    un = form.username.data
    pw = form.password.data
    user = User.query.filter_by(username=un).first()
    if user is None or not user.check_password(pw):
        flash('Invalid username or password')
        return redirect(url_for('forms.get_login_form'))
    else:
        login_user(user)
        flash('Logged in successfully!')
        return redirect(url_for('main.homepage'))


@forms_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('main.homepage'))


@forms_bp.route('/register', methods=['GET'])
def get_register_form():
    form = RegisterForm()
    return render_template('forms/register.html', form=form)


@forms_bp.route('/register', methods=['POST'])
def submit_register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        un = form.username.data
        em = form.email.data
        pw = form.password.data
        user = User(username=un, email=em, password=generate_password_hash(pw))
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully!")
        return redirect(url_for('main.homepage'))
    else:
        return render_template('forms/register.html', form=form)
