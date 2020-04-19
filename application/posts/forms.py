from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class PostForm(FlaskForm):
  content = TextAreaField("content", [
    validators.Length(min=3, max=280),
    validators.Regexp('.*\S+.*')
  ])

  class Meta:
    csrf = False
