from flask import render_template, url_for, flash, redirect, request, abort
from fold import app, db
from fold.forms import RegForm
from fold.models import User


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form=RegForm()
    if form.validate_on_submit():
            username=form.username.data
            email=form.email.data
            password=form.password.data
            confirm_password=form.confirm_password.data
            user=User( username=form.username.data , confirm_password=form.confirm_password.data , password=form.password.data ,email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('Your name has been saved', 'success')
            return render_template('home.html',form=form)
    return render_template('home.html',form=form)
