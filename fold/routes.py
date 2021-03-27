from flask import render_template, url_for, flash, redirect, request, abort
from fold import app, db
from fold.forms import RegForm,LoginForm,TransactionForm
from fold.models import User , Block_
from flask_login import login_user, current_user, logout_user, login_required
from blockchain import Blockchain , Block

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
    if form.validate_on_submit():
        amount=form.amount.data
        data=str(form.sender.data)+str(form.receiver.data)
        block=Block(number=amount,data=data)
        #
        # try:
        #     if n==0:
        #         pass
        # except:
        blockchain=Blockchain()
            # n=0
        blockchain.mine_block(block)
        block_=Block_(amount=amount,data=data,hash=block.hash(),nonce=block.nonce,previous_hash=block.previous_hash)
        # Block('22','ridtoney','0000000000000000000000000000000000000000000000000000000000000000','5004343')
        db.session.add(block_)
        # block_=Block_(id=block.id,amount=amount,data=data,hash=block.hash(),nonce=block.nonce,previous_hash=block.previous_hash)
        db.session.commit()
        # flash(Block_.query.filter_by(max(id)hash=block.hash()).last())
        flash("Your transaction is Successfull!")
        # flash(block_.amount)
        # flash(block_)
        for ock in Block_.query.all():
            if ock.id!=1:
                ock.previous_hash=a
            db.session.commit()
            a=ock.hash
        # id=db.Column(
    return render_template('transaction.html',form=form)

@app.route("/home/past_transactions", methods=['GET', 'POST'])
@login_required
def Past_transactions():
    flash(Block_.query.all())
    return render_template('past_transactions.html')



    # amount
    # data
    # hash
    # nonce
    # previous_hash
        # for block in blockchain.dd:
        #     flask("hii")
        #     flash(block)

        # block=Block(data=data,amount=amount)



# receiver
# sender
# amount
# submit
#
# amount
# id
# data
# hash
# nonce
# previous_hash
# @app.route("/home/blockchain", methods=['GET', 'POST'])
