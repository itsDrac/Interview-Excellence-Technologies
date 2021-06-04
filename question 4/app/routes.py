from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm, UpdateAccountForm
from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

@app.get('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.password == form.password.data:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html",form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('home'))
    form.email.data = current_user.email
    return render_template("account.html", form=form)
