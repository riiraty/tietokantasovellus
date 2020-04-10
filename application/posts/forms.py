from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PostForm(FlaskForm):
  title = StringField("Title", [
    validators.Length(min=3, max=64),
    validators.Regexp('.*\S+.*')
  ])
  content = TextAreaField("Post content", [
    validators.Length(min=3, max=280),
    validators.Regexp('.*\S+.*')
  ])

  class Meta:
    csrf = False

class EditForm(FlaskForm):
  content = TextAreaField("Edit post", [
    validators.Length(min=3, max=280),
    validators.Regexp('.*\S+.*')
  ])
  
  class Meta:
    csrf = False
