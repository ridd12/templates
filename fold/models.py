from fold import db,login_manager,app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=False,nullable=False)
    password=db.Column(db.String(20),unique=False,nullable=False)
    confirm_password=db.Column(db.String(20),unique=False,nullable=False)
    balance=db.Column(db.Integer,unique=False,nullable=False,default='100')
    db.session.commit()

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}','{self.password}')"
        # return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Block_(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    amount=db.Column(db.Integer,unique=False,nullable=False)
    data=db.Column(db.String(20),unique=False,nullable=False)
    hash=db.Column(db.String(64),unique=False,nullable=True)
    nonce=db.Column(db.Integer,nullable=True)
    previous_hash=db.Column(db.String(64),unique=False,nullable=True)
    db.session.commit()

    def __repr__(self):
        return f"Block('{self.id}','{self.amount}','{self.data}','{self.hash}','{self.nonce}','{self.previous_hash}')"
        # return f"User('{self.username}', '{self.email}', '{self.image_file}')"
#
# class Arr(db.model):
#     arr
