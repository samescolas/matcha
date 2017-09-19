from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators

class LoginForm(FlaskForm):
	email = StringField('Email Address', [validators.Length(min=4, max=32)])
	passwd = PasswordField('Password', [
		validators.DataRequired(),
		validators.Length(min=8, max=20)
	])
	remember = BooleanField('Remember me?')

class RegistrationForm(FlaskForm):
	email = StringField('Email Address', [validators.Length(min=4, max=32)])
	passwd = PasswordField('New Password', [
		validators.DataRequired(),
		validators.Length(min=8, max=20),
		validators.EqualTo('passwd2', message='Passwords must match')
	])
	passwd2 = PasswordField('Confirm Password')
