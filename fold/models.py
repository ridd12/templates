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
    db.session.commit()

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}','{self.password}')"
        # return f"User('{self.username}', '{self.email}', '{self.image_file}')"
