from flask import render_template, url_for, flash, redirect, request, abort
from fold import app, db
from fold.forms import RegForm,LoginForm,TransactionForm
from fold.models import User , Block_
from flask_login import login_user, current_user, logout_user, login_required
from blockchain import Blockchain , Block

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    users = User.query.all()
    # flash(users)
    return render_template('home.html',users=users)

@app.route("/logout")
def logout():
    logout_user()
    flash(' Your name have been logged out ! Please visit again ', 'success')
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html')

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
    form=LoginForm()
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

@app.route("/home/transaction", methods=['GET', 'POST'])
@login_required
def transaction():
    form=TransactionForm()
    # current_user.balance=10000
    # db.session.commit()
    if form.validate_on_submit():
        The_one=User.query.filter_by(username=form.receiver.data).first()
        The_two=User.query.filter_by(username=form.sender.data).first()
        if current_user.balance>=int(form.amount.data) and int(form.amount.data)>0 and current_user.balance>=0 and The_one!=None and The_two!=None and The_two.username==current_user.username :
            amount=form.amount.data
            data=str(form.sender.data)+str(form.receiver.data)
            block=Block(number=amount,data=data)
            blockchain=Blockchain()
            blockchain.mine_block(block)
            block_=Block_(amount=amount,data=data,hash=block.hash(),nonce=block.nonce,previous_hash=block.previous_hash)
            db.session.add(block_)
            db.session.commit()

            flash("Your transaction is Successfull!")
            for ock in Block_.query.all():
                if ock.id!=1:
                    ock.previous_hash=a
                db.session.commit()
                a=ock.hash
            current_user.balance-=int(form.amount.data)
            The_one.balance+=int(form.amount.data)
             # for testing purpose current_user.balance=10000
            db.session.commit()

        else:
            flash('Transaction not granted')
    return render_template('transaction.html',form=form)

@app.route("/home/past_transactions", methods=['GET', 'POST'])
@login_required
def Past_transactions():
    flash(Block_.query.all())
    return render_template('past_transactions.html')
