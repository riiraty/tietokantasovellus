from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
  username = StringField("Username", [
    validators.Length(min=3, max=32)
  ])
  password = PasswordField("Password", [
    validators.Length(min=3, max=32)
  ])
  
  class Meta:
    csrf = False

class SignUpForm(FlaskForm):
  username = StringField("Username", [
    validators.Length(min=3, max=32)
  ])
  password = PasswordField("New password", [
    validators.Length(min=6, max=32),
    validators.EqualTo('confirm', message='Passwords must match')
  ])
  confirm = PasswordField("Repeat password")
  
  class Meta:
    csrf = False