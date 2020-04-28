from application import db
from sqlalchemy.sql import text, func

class Thread(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  creation_time = db.Column(db.DateTime, default=db.func.current_timestamp())
  modification_time = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

  title = db.Column(db.String(64), nullable=False)

  owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
  posts = db.relationship("Post", backref='thread', lazy=True)

  def __init__(self, title):
    self.title = title