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