from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fold.models import User



class RegForm (FlaskForm) :
    username = StringField('Username',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm) :
    username_or_email=StringField('username_or_email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Register')

class TransactionForm(FlaskForm) :
    receiver=StringField('receiver',validators=[DataRequired()])
    sender=StringField('sender',validators=[DataRequired()])
    amount=StringField('amount',validators=[DataRequired()])
    submit = SubmitField('pay')
