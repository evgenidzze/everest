from flask import redirect, url_for, flash, render_template, session
from flask_login import login_user, login_required, logout_user

from market import app, db, login_manager
from market.forms import RegisterForm, LogInForm
from market.models import User


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    else:
        for err_msg in form.errors.values():
            flash(f"Error with creating user: {err_msg}", category='danger')
    return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    session['logged_in'] = True
    form = LogInForm()
    print(form.username.data)
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are signed in as: {attempted_user.username}', category='success')
            return redirect(url_for('catalog_page'))
        else:
            flash(f'Username and password are not match! Please try again.', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    del session['logged_in']
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('catalog_page'))
