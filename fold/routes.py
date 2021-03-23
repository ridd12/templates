from flask import render_template, url_for, flash, redirect, request, abort
from fold import app, db
from fold.forms import RegForm,loginForm
from fold.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/logout")
def logout():
    logout_user()
    flash(' Your name have been logged out ! Please visit again ', 'success')
    return redirect(url_for('home'))


@app.route("/registraion", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegForm()
    if form.validate_on_submit():
            username=form.username.data
            email=form.email.data
            password=form.password.data
            confirm_password=form.confirm_password.data
            user=User( username=form.username.data , confirm_password=form.confirm_password.data , password=form.password.data ,email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash(' Your data has been saved ', 'success')
            # return render_template(url_for("login"))
            return redirect(url_for('login'))
    return render_template('register.html',form=form)




@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=loginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(username=form.username_or_email.data).first()
            if user and user.password==form.password.data:
                login_user(user)
                next_page = request.args.get('next')
                flash('You have been loged in', 'success')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            user = User.query.filter_by(email=form.username_or_email.data).first()
            if user and user.password==form.password.data:
                login_user(user)
                next_page = request.args.get('next')
                flash(' You have been loged in', 'success')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:flash('Check your email or password')
    return render_template('login.html',form=form)
# @app.route("/", methods=['GET', 'POST'])
# def about():
#     form=logoutForm()
#     if form.validate_on_submit():
#             flash(' Loged out ! Please visit us again ', 'success')
#             return render_template('login.html',form=form)
#     return render_template('home.html',form=form)
