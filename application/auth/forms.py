from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
  username = StringField("Username", [
    validators.Length(min=3, max=26,
      message='Username is between 3 and 26 characters long.')
  ])
  password = PasswordField("Password", [
    validators.Length(min=7, max=256,
      message='Your password is at least 7 characters.')
  ])
  
  class Meta:
    csrf = False

class SignUpForm(FlaskForm):
  username = StringField("Username", [
    validators.Length(min=3, max=26),
    validators.Regexp('^[a-zA-Z0-9_]*$',
      message='Username can contain letters, numbers and underscores (_).')
  ])
  password = PasswordField("New password", [
    validators.Length(min=7, max=256,
      message='Password must be at least 7 characters long.'),
    validators.Regexp('^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)(?=.*[@$!%*#?&]+.*)[0-9a-zA-Z@$!%*#?&]{7,}$',
      message='Password must contain a letter, a number and a special character (@$!%*#?&).'),
    validators.EqualTo('confirm', message='Passwords must match.')
  ])
  confirm = PasswordField("Repeat password", [
    validators.InputRequired(message='You must repeat the password.')
  ])
  
  class Meta:
    csrf = False