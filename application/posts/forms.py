from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class PostForm(FlaskForm):
  content = TextAreaField("Post content", [validators.Length(min=3, max=280)])

  class Meta:
    csrf = False

class EditForm(FlaskForm):
  content = TextAreaField("Edit post content", [validators.Length(min=3, max=280)])
  
  class Meta:
    csrf = False
