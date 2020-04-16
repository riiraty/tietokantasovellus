from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ThreadForm(FlaskForm):
  title = StringField("Title", [
    validators.Length(min=3, max=64),
    validators.Regexp('.*\S+.*')
  ])
  content = TextAreaField("Your post", [
    validators.Length(min=3, max=280),
    validators.Regexp('.*\S+.*')
  ])

  class Meta:
    csrf = False