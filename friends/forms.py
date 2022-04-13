from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from friends.models import Friends
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email',
        validators=[DataRequired(), Email(), Length(min=6, max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=16)])
    confirm_password = PasswordField('Comfirm Password',
                                     validators=[DataRequired(), Length(min=6, max=16), EqualTo('password')])
    submit = SubmitField('Sign up to become a Friend')

    def validate_username(self, username):

        friend = Friends.query.filter_by(username=username.data).first()
        if friend:
            raise ValidationError('Username exist please choose another one')
    #need to debug this code for later version 1.1 haha, damn thing kills in validig a second account ugh
    #def validate_email(self, email):

    #    friend = Friends.query.filter_by(email=email.data).first()
    #    if email:
    #        raise ValidationError('Email exist please provide a different one')

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=16)])
    remember_session = BooleanField('Stay Logged In')
    submit = SubmitField('Login')

class ProfieUpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email',
        validators=[DataRequired(), Email(), Length(min=6, max=100)])
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        if username.data != current_user.username:
            friend = Friends.query.filter_by(username=username.data).first()
            if friend:
                raise ValidationError('Username exist please choose another one')