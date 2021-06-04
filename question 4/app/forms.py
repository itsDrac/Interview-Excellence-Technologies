from app.models import User
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    register = SubmitField('Sign Up')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This Email Is Already Taken')

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    login = SubmitField('Log In')



class UpdateAccountForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()])
    update = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This Email Is Already Taken')
