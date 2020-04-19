from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ThreadForm(FlaskForm):
  title = StringField("title", [
    validators.Length(min=3, max=60),
    validators.Regexp('.*\S+.*')
  ])
  content = TextAreaField("content", [
    validators.Length(min=3, max=280),
    validators.Regexp('.*\S+.*')
  ])

  class Meta:
    csrf = False